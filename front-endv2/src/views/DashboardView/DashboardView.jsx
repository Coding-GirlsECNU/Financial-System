import { defineComponent, ref, watch } from "vue";
import { useRoute } from "vue-router";
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'
import DecChart from "@/components/charts/DecChart.vue";

export const DashboardView = defineComponent({

    setup() {
        let route = useRoute()
        let itemRefs = ref([])
        let autoFetch = ref(false)
        let timer = ref(null)
        function GenNonDuplicateID() {
            return Math.random().toString()
        }
        watch(autoFetch, (newVal, oldVal) => {
            if (newVal === true) {
                timer.value = setInterval(() => {
                    refreshCall()
                }, 10000)
            } else {
                clearInterval(timer.value)
            }
        })
        const setRef = (el) => {
            if (el) {
                itemRefs.value.push(el)
            }
        }



        let refreshCall = () => {
            itemRefs.value.forEach(item => {
                item.refreshData()

            })
        }
        let query = JSON.parse(route.query.config)
        let layout = query.layout
        let rowNum = ref([])
        rowNum.value = layout
        function splitArray(arr, lengths) {
            let result = [];
            let index = 0;

            for (const length of lengths) {
                result.push(arr.slice(index, index + length));
                index += length;
            }

            return result;
        }

        const lengths = rowNum.value.map(subArray => subArray.length);
        const charts = ref(splitArray(query.charts, lengths));
        charts.value = charts.value.filter(row => row.length > 0)

        function resizeChart() {
            itemRefs.value.forEach(item => {
                item.resize()
            })
        }



        return () => <>
            <div class={'w-full h-full'}>
                <div class="bg-white h-12 w-full">
                    <div class="flex justify-around w-full">
                        <div>
                            <span class="font-600  space-x-2">
                                <el-tag>刷新数据 ：</el-tag>
                                <el-icon onClick={refreshCall} class="cursor-pointer text-xl mt-1">
                                    <Refresh />
                                </el-icon>
                            </span>
                        </div>
                        <div>
                            <span class="font-600  space-x-2">
                                <el-tag>自动刷新 ：</el-tag>
                            </span>
                            <el-switch v-model={autoFetch.value} />
                        </div>
                    </div>
                </div>
                <div class={'w-full h-screen'}>
                    <Splitpanes class={"default-theme w-full h-full"} horizontal onResized={(evt) => { resizeChart() }}>
                        {charts.value.map((rowCharts, idx) => <Pane rowId={idx}>
                            <Splitpanes class={'w-full h-full '} onResized={(evt) => { resizeChart() }}>
                                {rowCharts.map((item, col_idx) =>
                                    <Pane  >
                                        <DecChart chart={GenNonDuplicateID()}
                                            class="w-full h-full" dataset={item.dataset}
                                            mapping={item.mapping}
                                            ctype={item.config.type}
                                            ref={setRef}
                                        >
                                        </DecChart>
                                    </Pane>

                                )}
                            </Splitpanes>

                        </Pane>)}
                    </Splitpanes>
                </div>
            </div >

        </>




    }

})
