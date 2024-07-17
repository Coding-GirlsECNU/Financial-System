<template>
  <div class="w-full h-screen">
      <div class="flex justify-start" style="margin-left: 25px;margin-top: 18px;">
          <div class="module-border-wrap flex items-center">
              <div class="module" style="margin-left: 6px; width: 100px;">
                  <span class="blink">选择策略</span>
              </div>
              <el-select v-model="selectedModel" style="margin-left: 6px; width: 350px;">
                  <el-option v-for="val in models" :key="val.id" :value="val.model_name">
                      {{ val.model_name }}
                  </el-option>
              </el-select>
              <div class="flex gap-8" style="margin-left: 10px;margin-right: 8px;">
                  <div>
                      <el-button type="primary" @click="confirm">开始绘制</el-button>
                  </div>
              </div>
          </div>
          <div class="module-border-wrap">
              <div class="module">
                  说明：若使用PatchTST&Factors模型，还会展示因子变量
              </div>
          </div>
      </div>
      <div class="h-1/2 border-gray-400 bg-sky-50" style="margin-top: 18px; max-width: 1210px;">
                      <SingleLineChart_sharpe v-if="linerdata && linerdata.length > 0" :formData="linerdata" :chart="'SLC'" ref="chartRef" :mapping="mapping"/>
                  </div>
      <!--这边添加图标-->
      <div class="w-full h-full flex justify-center items-center">
          <div style="width: 80%; height: 80%;">
              <div style="display: grid; grid-template-columns: 1fr 800px 1fr; grid-template-rows: auto; grid-gap: 120px;">

              </div>
          </div>

      </div>

      <div class="w-full h-full" style="margin-top: -300px;">
          <div style="width: 100%; height: 100%;">         
              <div style="display: grid; grid-template-columns: 1fr 700px 1fr; grid-template-rows: auto;">
                  
                  <!-- <span style="background-color: white; grid-column: 2 ; position: relative;">
                      <img src="image1.jpg" alt="Image 3" style="width: 100%; height: 100%; object-fit: cover;">
                  </span> -->
              </div>
          </div>
      </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { execQuery } from '@/api/sqllab/utils';
import { axios } from '../../api/axios'
import { useBootstrapStore } from '../../stores/counter';
import { ElMessage } from "element-plus";
import ConfigList from '../../components/algorithm/ConfigList.vue'
import DecChart from '../../components/charts/DecChart.vue';
import { saveDataset } from "@/api/sqllab/utils";
import SingleLineChart_sharpe from '@/components/charts/SingleLineChart_sharpe.vue';
import dayjs from "dayjs";
let bootstrap = useBootstrapStore();
let models = ref(bootstrap.bootstrap.models);
let datasets = ref(bootstrap.bootstrap.dataset);
let mapping = ref([])
let modelConfig = ref({});

let linerdata=ref([])
const chartRef = ref();

let selectedModel = ref(null);

let selectedDataset = ref(null)
let example = ref(null)
//加上selectDataset
watch(selectedModel, (val, oldVal) => {

  let model = models.value.filter(model => model.model_name === val)[0]
  mapping.value = model.model_config.input
  example.value = model.model_config.example

})
let handleConfig = (arg) => {
  arg.forEach(item => {
      modelConfig.value[item[0]] = item[1]
  })
}
mapping={
          "x_orient":["x_orient"],
          "date":["date"]
      }
let confirm = () => {

  if (chartRef.value){
  setTimeout(() => {
    chartRef.value.refreshData()
  }, 500);

}

  fetchData_liner().then(res => {
      linerdata.value = res;
      });
      console.log("linerdata",linerdata)
}

let fetchData_liner = async () => {

let query_total="SELECT * FROM public.\"total_value\" WHERE \"strategy\"='modelName' ORDER BY date ASC"

const newQuery_total = query_total.replace('modelName', selectedModel.value);
const newData_total = {
database: "al",
host: "47.95.213.242",
password:"zzh0117.",
port:"5433",
query:newQuery_total,
type: "psql",
user: "postgres"
}
console.log("total_config",newData_total)
let total_table = await execQuery(newData_total)
console.log("total",total_table.data)
const totalData = total_table.data;
// 创建一个空数组用于存储合并后的数据
let newTable = [];
for (let i = 0; i < totalData.length; i++) {
let newData = {};

// 设置日期属性
newData.date = totalData[i].date;

// 设置实际值属性
newData.x_orient = totalData[i].sharpe;

// 将新对象添加到数组中
newTable.push(newData);
}

return newTable
}

</script> 

<style scoped>
.border-solid {
  border: solid;
}
.styled-span {

  font-family: Arial;
  font-size: 24px;
  margin-top: 15px;

}

.styled-button {
  background-color: #4CAF50;
  color: white;
  font-family: Arial;
  font-size: 30px;
  border: 15px solid #4CAF50; /* 设置边框大小和颜色 */
  margin-top: 15px; /* 向下移动位置 */
}

body {
height: 200vh;
margin: 0;
display: grid;
place-items: center;
background: #263544;
}

.module-border-wrap {
max-width: 500px;
padding: 1rem;
position: relative; 
top: 1.5vh; /* 调整垂直位置 */
padding: 3px;
}


.image3-wrapper{
  margin-top: 10px;
}

.module {
background: #263544;
color: white;
padding: 0.7rem;
margin-left: 8px;
font-size: 18px;
-webkit-text-stroke:0.3px #e0edfa;
}

@keyframes blink {
  0% { opacity: 1; }
  50% { opacity: 0; }
  100% { opacity: 1; }
}

.blink {
  animation: blink 1s;
  animation-duration: 5s;  
}
</style>