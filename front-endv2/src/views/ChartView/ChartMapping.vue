<template>
    <div class="w-full h-full flex bg-slate-100">
        <div class="w-1/4 h-full bg-slate-100 flex flex-col space-y-4">

            <div class="ml-3" v-for="(item, idx) in chartConfig">
                <div class="m-2 text-lg">{{ item.label }}</div>
                <el-select multiple v-if="item.type === 'select'" :placeholder="item.desc" v-model="item.axis">
                    <el-option v-for="item in dataCols" :label="item" :value="item">
                    </el-option>
                </el-select>
                <el-input v-else :placeholder="item.desc" v-model="item.axis"></el-input>
            </div>

            <div class="p-4 space-y-3">
                <div class="w-full">
                    <el-button class="w-full" type="primary" @click="confirm">确认</el-button>
                </div>
                <div class="w-full">
                    <el-button class="w-full" type="default" @click="handleOpenModal">保存</el-button>
                </div>
            </div>
        </div>
        <div class="w-3/4 border-gray-400 h-full bg-sky-50">
            <dec-chart v-if="showChart" :ctype="chart" :dataset="dataset" :mapping="mapping" />
        </div>
        <el-dialog v-model="saveChartModal" class="w-1/3">
            <el-form>
                <el-form-item label="图表名称">
                    <el-input v-model="saveChartName"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <div>
                    <el-button type="primary" @click="handleSaveChart">
                        确认
                    </el-button>
                </div>

            </template>

        </el-dialog>

    </div>
</template>
 
<script setup>
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router';
import { useBootstrapStore } from '@/stores/counter';
import DecChart from '../../components/charts/DecChart.vue';
import { saveChart } from "@/api/chart/chartApi";
const bootstrapStore = useBootstrapStore();
let route = useRoute();
const { query } = route;
let dataset = ref(JSON.parse(query.dataset))
let dataCols = ref(Object.keys(dataset.value.example_row))
let chart = ref(query.chart)
let chartTemplate = ref(bootstrapStore.bootstrap.chart_template)
let chartConfig = ref(chartTemplate.value.filter(item => item.chart_name === chart.value)[0]?.config.template)
let mapping = ref({})
let showChart = ref(false)
let saveChartModal = ref(false)
let saveChartName = ref('')
let confirm = () => {
    let tmp = {}
    for (let i = 0; i < dataCols.value.length; i++) {
        tmp[chartConfig.value[i]?.value] = chartConfig.value[i]?.axis
    }
    mapping.value = tmp
    showChart.value = true

}

let handleOpenModal = () => {
    saveChartModal.value = true
}
let handleSaveChart = () => {
    let cfg = { "type": chart.value }
    chartConfig.value.forEach(item => {
        let type = item.type
        if (type !== 'select') {
            cfg[item.label] = item.axis
        }
    })
    cfg.name = saveChartName.value;
    let payload = {
        config: cfg,
        dataset: dataset.value,
        mapping: mapping.value
    }
    saveChart(payload).then(res => {
        saveChartModal.value = false
        saveChartName.value = ''
    })
}
</script>
 
<style scoped></style>