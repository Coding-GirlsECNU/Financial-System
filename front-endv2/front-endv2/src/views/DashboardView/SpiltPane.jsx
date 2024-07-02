import { defineComponent, onMounted, ref } from 'vue';
import DecChart from "@/components/charts/DecChart.vue";
import { saveBoard } from "@/api/dashboard/dashboardApi";
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import { ElMessage } from "element-plus";
export const Board = defineComponent({
    props: {
        chart: Array
    },
    setup(props) {


        let rowNum = ref([])
        let dragItem = ref(null)

        let chart = props.chart
        let dashboardName = ref('')

        const drag = () => {
            let el = document.querySelectorAll('.dec-chart')
            el.forEach(item => {
                item.addEventListener('drag', (event) => {
                    dragItem.value = event.target
                })
                item.addEventListener('dragstart', (event) => {
                    dragItem.value = event.target
                })
            })
        }

        const addDragTarget = () => {
            let el = document.querySelectorAll('.drag-target')
            el.forEach(item => {
                // add a new attribute to the element
                if (item.getAttribute('ondrop') !== null) {
                    return
                }
                item.setAttribute('ondrop', '1')
                item.addEventListener('drop', (event) => {
                    event.preventDefault();
                    console.log('drop drop drop', dragItem.value, event.target.parentNode)
                    let charId = dragItem.value.getAttribute('chartId')
                    let rowId = event.target.parentNode.parentNode.getAttribute('rowId')
                    rowNum.value[rowId].push(charId)
                })
                item.addEventListener('dragover', (event) => {
                    event.preventDefault();
                }, false)
            })
        }
        const addRow = () => {
            rowNum.value.push([])
            addDragTarget()
        }
        function GenNonDuplicateID() {
            return Math.random().toString()
        }
        onMounted(() => {
            drag()
            addDragTarget()

        })

        const saveDashboard = () => {
            if (dashboardName.value === '') {
                ElMessage.warning('dashboard name cannot be empty')
                return
            }
            let data = {
                dashboard_name: dashboardName.value,
                charts: [],
                layout: rowNum.value,
            }
            let el = document.querySelectorAll('.dec-chart')
            let shapeList = []
            el.forEach(item => {
                // get item width and height
                let width = item.offsetWidth
                let height = item.offsetHeight
                shapeList.push({
                    width: width,
                    height: height,
                })
            })
            rowNum.value.forEach((row, rowId) => {
                row.forEach((col, colId) => {
                    data.charts.push(chart[col])
                })
            })
            saveBoard(data).then(res => {
                let response = res.data
                if (response.code === 200) {
                    ElMessage.success('save success')
                }
                console.log(res)
            })
        }
        return () => (
            <>
                <div class="w-full h-full  ">
                    <div class={'w-full h-10 bg-white flex justify-start gap-10'}>
                        <div>
                            <el-button onClick={() => { saveDashboard() }}>保存大屏</el-button>
                        </div>
                        <div>
                            <el-input v-model={dashboardName.value} placeholder="大屏名称"></el-input>
                        </div>
                    </div>
                    <div class={'w-full h-full flex'}>
                        <div class="w-5/6 h-screen flex bg-slate-50">
                            <Splitpanes class={"default-theme w-full h-full"} horizontal>
                                {rowNum.value.map((row, idx) => <Pane rowId={idx}>
                                    <Splitpanes class={'w-full h-full '}>
                                        {row.map((col, col_idx) =>
                                            <Pane >
                                                <DecChart chart={GenNonDuplicateID()}
                                                    class="w-full h-full " dataset={chart[col].dataset}
                                                    mapping={chart[col].mapping}
                                                    ctype={chart[col].config.type}
                                                >
                                                </DecChart>
                                            </Pane>

                                        )}
                                        <Pane class={'drag-target   border-dashed border-gray-300 text-center m-auto '}>
                                            <span class={'text-gray-400'}>
                                                拖拽到此处,最后一行/列默认不显示
                                            </span>
                                        </Pane>

                                    </Splitpanes>

                                </Pane>)}
                            </Splitpanes>

                        </div>
                        <div class=" w-1/6 h-full overflow-y-scroll flex flex-col gap-5 bg-slate-200">
                            <el-button onClick={addRow} >添加行</el-button>
                            {chart.map((item, idx) => {
                                return <div class={'w-full h-20 dec-chart'} draggable="true" chartId={idx}>
                                    <DecChart chart={'ch_' + (idx + 8928).toString()}
                                        class="w-full h-full" dataset={item.dataset}
                                        mapping={item.mapping}
                                        ctype={item.config.type}
                                        mode='tooltip_disable'
                                    >
                                    </DecChart>
                                </div>
                            })}
                        </div>
                    </div>

                </div >
            </>
        )
    }
})