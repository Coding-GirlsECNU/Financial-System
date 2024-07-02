<template>
    <div class="w-full h-full">
        <TimeSeries v-if="data && data.length > 0 && props.ctype === 'TSL'" class="w-full h-full"
            :is="props.ctype === 'TSL'" :form-data="data" :chart="props.chart" :mode="mode" ref="chart"
            :mapping="props.mapping" />
        <LinePredictChart v-if="data && data.length > 0 && props.ctype === 'LPC'" class="w-full h-full"
            :is="props.ctype === 'LPC'" :form-data="data" :chart="props.chart" :mode="mode" ref="chart"
            :mapping="props.mapping" />
        <TableChart v-if="data && data.length > 0 && props.ctype === 'Table'" class="w-full h-full"
            :is="props.ctype === 'Table'" :form-data="data" :mapping="props.mapping" :mode="mode" ref="chart" />

    </div>
</template>
 
<script setup>
import { ref, onMounted } from 'vue'
import { transferMapping } from '@/utils/utils';
import { execQuery } from '@/api/sqllab/utils';
import LinePredictChart from "@/components/charts/LinePredictChart.vue";
import TableChart from './TableChart.vue';
import TimeSeries from '@/components/charts/TimeSeries.vue';
let data = ref([])
let chart = ref()
const props = defineProps(
    {
        ctype: {
            type: String,
            default: '',
            required: true
        },
        mapping: {
            type: Object,
            default: {},
            required: true
        },
        dataset: {
            type: Object,
            default: {},
            required: true
        },
        chart: {
            type: String,
            default: "proChart",
        },
        mode: {
            type: String,
            default: "normal"
        }
    }
)

let fetchData = async () => {
    let datasource = props.dataset.config
    let result = await execQuery(datasource)
    // let trans = transferMapping(result.data, props.mapping)
    // return trans
    return result.data
}
fetchData().then(res => {
    data.value = res
})
const refreshData = () => {
    fetchData().then(res => {
        data.value = res
    }).then(() => {
        chart.value.refreshData()
    })
}
const resize = () => {
    if (chart.value) {
        chart.value.resizeWindow();
    }
}
defineExpose({
    refreshData,
    resize
})
onMounted(() => {


})

</script> 
 
<style scoped></style>