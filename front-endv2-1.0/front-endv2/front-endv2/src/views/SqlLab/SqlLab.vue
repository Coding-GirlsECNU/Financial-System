<template>
    <div class="w-full h-screen ">
        <div class="flex justify-evenly h-3/5">
            <div class="border-1 border-slate-300 w-1/3 h-full " style="border:  1px solid;">
                <el-descriptions class="p-2" title="数据库信息">
                    <el-descriptions-item :label="item[0]" v-for="item in Object.entries(query)">
                        {{ item[1] }}
                    </el-descriptions-item>
                </el-descriptions>
                <div>
                    <div class="p-2">
                        数据库表
                    </div>
                    <el-select class="p-2" v-model="activateTable">
                        <el-option v-for="item, idx in tables" :key="idx + 234" :label="item.table" :value="item.table" />
                    </el-select>
                    <el-descriptions class="p-2" title="表信息">
                        <el-descriptions-item label="列名 " v-for="item in tableInfo">
                            {{ item }}
                        </el-descriptions-item>
                    </el-descriptions>
                </div>
            </div>
            <div class="w-1/2 h-full">
                <Editor class="w-full h-full" cid="editor" v-model="content" />
            </div>
        </div>
        <div class="flex flex-row-reverse m-5">
            <el-button type="primary" class="mr-5 pr-5" @click="runQuery"> Run Query</el-button>
            <el-button class="mr-5 pr-5" @click="saveClick"> Save Dataset </el-button>
        </div>
        <div>
            <MyHeader content="查询结果" />
            <div class="w-full m-auto">
                <el-table class="w-full max-h-44 overflow-y-scroll overflow-x-hidden " :data="queryRes">
                    <el-table-column v-for="key, idx in tableCol " :prop="key" :label="key">
                    </el-table-column>
                </el-table>
            </div>
        </div>
        <el-dialog v-model="showModal">
            <div>
                输入数据集名称
            </div>
            <el-input placeholder="输入数据集名称" v-model="datasetName"></el-input>
        </el-dialog>
    </div>
</template>
 
<script setup>
import Editor from '../../components/sqllab/Editor.vue';
import { useRoute } from 'vue-router';
import { getDatasrcMeta, execQuery, saveDataset } from "../../api/sqllab/utils"
import { ref, watch, h } from 'vue'
import { ElMessage, ElMessageBox, ElInput, ElButton } from 'element-plus'
import MyHeader from '../../components/trivial/MyHeader.vue';
let content = ref('')
let tables = ref([])
let activateTable = ref(null)
let tableInfo = ref(null)
let queryRes = ref([])
let tableCol = ref([])
let showModal = ref(false)
let datasetName = ref('')
const { query } = useRoute()
let fetchDataSrcMeta = () => {
    getDatasrcMeta(query).then(res => {
        tables.value = res.data
    })
}
watch(activateTable, (newVal, oldVal) => {
    let tmp = tables.value.filter(item => {
        return item.table === newVal
    })
    tableInfo.value = tmp[0].detail
})
let runQuery = () => {
    query['query'] = content.value
    execQuery(query).then(res => {
        if (res.status !== 200) {
            ElMessage.error(res.data.msg)
            return
        }
        queryRes.value = res.data
        tableCol.value = Object.keys(queryRes.value[0])
    }).catch(err => {
        ElMessage.error(err)

    })
}
let saveClick = () => {
    if (content.value === '') {
        ElMessage.error('请先输入查询语句')
        return
    }
    if (queryRes.value.length === 0) {
        ElMessage.error('请先执行查询语句 or 数据集为空')
        return
    }
    ElMessageBox({
        title: '数据集信息',
        message: () =>
            h('div', null, [
                h('div', null, [
                    h('span', null, '数据集名称'),
                    h(ElInput, {
                        placeholder: '请输入数据集名称',
                        modelValue: datasetName.value,
                        'onUpdate:modelValue': (val) => {
                            datasetName.value = val
                        },
                    }),
                ])
            ]
            ),
        confirmButtonText: '确定'
    }).then(() => {
        let dataset = {
            query: content.value,
            example_row: queryRes.value[0],
            config: query,
            dataset_name: datasetName.value
        }
        saveDataset(dataset).then(res => {
            if (res.status !== 200) {
                ElMessage.error(res.data.msg)
                return
            }
            ElMessage.success('保存成功')
        }).catch(err => {
            ElMessage.error(err)
        })
    }).catch(action => {
        ElMessage.info('取消保存')
    })

}
fetchDataSrcMeta()
</script> 
 
<style scoped></style>