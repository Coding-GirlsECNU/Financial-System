<template>
  <div class="w-full h-full">
    <div class="flex h-20">
      <el-steps class="w-full" :active="active" align-center>
        <el-step title="步骤一" description="选择数据源" />
        <el-step title="步骤二" description="选择图表" />
      </el-steps>

    </div>
    <div v-if="active === 1">
      <div>
        <my-header content="选择数据集"></my-header>
      </div>
      <div class="flex gap-x-4">
        <div>
          <el-select v-if="options" v-model="value" class="m-2" placeholder="Select" size="large">
            <el-option v-for="item in options" :key="item.id" :label="item.dataset_name" :value="item.datasetid" />
          </el-select>
        </div>
        <div>
          <el-button class="m-3" type="primary" @click="goNext">下一步</el-button>
        </div>
      </div>
      <div v-if="options.filter(item => item.datasetid == value)[0]?.example_row">
        <el-table :data="[options.filter(item => item.datasetid == value)[0]?.example_row]">
          <el-table-column
            v-for="(item, idx) in Object.keys(options.filter(item => item.datasetid == value)[0]?.example_row)" :key="idx"
            :prop="item" :label="item">
          </el-table-column>
        </el-table>
      </div>
      <my-header content="图表集合"></my-header>
      <div v-if="charts.length > 0" class="grid grid-cols-3 w-full h-full   m-0">
        <div v-for="item in charts" class="w-10/12 h-52 mt-5">
          <div class="w-full h-full shadow-lg">
            <div class="w-full h-2/3 ">
              <dec-chart class="w-full h-11/12" :chart="GenNonDuplicateID()" :dataset="item.dataset"
                :mapping="item.mapping" :ctype="item.config.type" :mode="'pic'" />
            </div>
            <div class="w-full h-1/3 mt-1">
              <div class="text-gray-500 text-center ">
                {{ item.config.name }}
              </div>
              <div class="text-center">
                <el-icon class=" cursor-pointer text-lg text-red-500 mt-2"
                  @click="() => { handleDeleteChart(item.chartid) }">
                  <Delete />
                </el-icon>
                <!-- <el-button type="danger" ">delete</el-button> -->
              </div>
            </div>
          </div>
        </div>

      </div>


    </div>
    <div v-if="active === 2">
      <my-header content="选择图表"></my-header>
      <div class="flex gap-4">
        <div>
          <el-button @click="active = 1">上一步</el-button>
        </div>
        <div>
          <el-button type="primary" @click="confirm">确认</el-button>
        </div>
      </div>
      <div class="m-4">
        <el-select v-model="chartValue" class="m-4">
          <el-option v-for="item in chartOption" :key="item" :label="item" :value="item" />
        </el-select>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBootstrapStore } from '../../stores/counter';
import MyHeader from '../../components/trivial/MyHeader.vue'
import { ElMessage } from 'element-plus';
import { useRouter } from 'vue-router'
import { deleteChart, getAllChart } from "@/api/chart/chartApi";
import DecChart from "@/components/charts/DecChart.vue";
import { GenNonDuplicateID } from '../../utils/utils';

const router = useRouter()
const bootstrapStore = useBootstrapStore();
let options = ref(bootstrapStore.bootstrap.dataset);
//TODO: // replace chart with real data
let chartOption = ref(['TSL', 'LPC', 'Table'])
let chartValue = ref([])
let value = ref(null);
let active = ref(1)
let charts = ref([])
getAllChart().then(res => {
  charts.value = res.data.data
})
let goNext = () => {
  if (value.value) {
    active.value = 2
  } else {
    ElMessage.error('Please choose a dataset')
  }
}
let confirm = () => {
  let selectedDataset = options.value.filter(item => item.datasetid == value.value)[0]
  let selectedChart = chartValue.value
  router.push({ name: 'chartmapping', query: { dataset: JSON.stringify(selectedDataset), chart: selectedChart } })
}
let handleDeleteChart = (payload) => {
  deleteChart(payload).then(res => {
    let response = res.data
    if (response.code === 200) {
      ElMessage.success('delete success')
      charts.value = response.data
    } else {
      ElMessage.error('delete failed')
    }
  })
}

</script>

<style scoped></style>