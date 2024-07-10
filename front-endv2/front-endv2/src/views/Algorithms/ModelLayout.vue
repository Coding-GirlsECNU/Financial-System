<template>
    <div class="w-full h-screen">
        <div class="flex justify-start" style="margin-left: 25px;margin-top: 18px;">
            <div class="module-border-wrap flex items-center">
                <div class="module">
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

            <!--<div class="styled-span">
                <span>
                    选择数据集
                </span>
                <el-select v-model="selectedDataset">
                    <el-option v-for="(val, idx) in datasets" :key="idx + 2324" :label="val.dataset_name"
                        :value="val.datasetid">
                        {{ val.dataset_name }}
                    </el-option>
                </el-select>
            </div>-->
        </div>
        
        <div class="w-full h-full">
            <el-row :gutter="20" class="w-full h-1/3">
                <el-col :span="20" class="w-full h-1/3" v-if="selectedModel" style="margin-left: 10px; margin-top: 20px;">
                    <ConfigList @confirmUpdate="handleConfig" class="border-solid border-2 border-gray-200 w-full mt-4 ml-4 config-list"
                        v-if="models.filter(model => model.model_name === selectedModel)[0]"
                        :config="models.filter(model => model.model_name === selectedModel)[0]?.model_config1">
                    </ConfigList>
                </el-col>
                <el-col :span="20" class="w-full h-full mt-12">
                    <div class="h-full border-gray-400 bg-sky-50" style="margin-left: 21px;width: 1200px;">
                        <SingleLineChart v-if="linerdata && linerdata.length > 0" :formData="linerdata" :chart="'SLC'" ref="chartRef" :mapping="mapping"/>
                    </div>
                </el-col>
                <el-col :span="20" class="w-full h-full mt-12" style="margin-left: 20px;">
                    <el-date-picker v-model="chooseDate" type="date" placeholder="选择日期" :disabled-date="checkAllowedDates" :defaultValue="start_date" @change="dateChange"> 
                    </el-date-picker>
                </el-col>
                <el-table :data="tableData" border style="width: 1200px; margin-top: -190px; margin-left: 28px;" class="bg-sky-50">
                    <el-table-column prop="stock" label="股票名称"></el-table-column>
                    <el-table-column prop="rank" label="排名"></el-table-column>
                </el-table>
            </el-row>
            <!-- <el-table :data="tableData" border style="width: 1200px; margin-top: 180px; margin-left: 20px;" class="bg-sky-50">
                <el-table-column prop="stock" label="股票名称"></el-table-column>
                <el-table-column prop="rank" label="排名"></el-table-column>
            </el-table> -->
        </div>
        <!-- <div class="w-full h-full" style="margin-top: -250px; margin-left: 20px; ">
            <el-table :data="tableData" border style="width: 1200px;" class="bg-sky-50">
            <el-table-column prop="stock" label="股票名称"></el-table-column>
            <el-table-column prop="rank" label="排名"></el-table-column>
        </el-table>
        </div> -->
    </div>
</template>
 
<script setup>
import { execQuery } from '@/api/sqllab/utils';
import { ref, watch } from 'vue'
import { axios } from '../../api/axios'
import { useBootstrapStore } from '../../stores/counter';
import { ElMessage } from "element-plus";
import ConfigList from '../../components/algorithm/ConfigList.vue'
import SingleLineChart from '@/components/charts/SingleLineChart.vue';
import DecChart from '../../components/charts/DecChart.vue';
import { saveDataset } from "@/api/sqllab/utils";
import dayjs from "dayjs";
let bootstrap = useBootstrapStore();
let models = ref(bootstrap.bootstrap.models);
let datasets = ref(bootstrap.bootstrap.dataset);
let mapping = ref([])
let modelConfig = ref({});
let date_range = ref([]) 
let dateString=ref([])
let selectedModel = ref(null);
let chooseDate=ref([])
let example = ref(null)
let linerdata=ref([])
let tableData=ref([])
const start_date = ref(null);
const chartRef = ref();
let get_datelist = async () => {
  // 全部日期
  const date_config = {
    database: "al",
    host: "47.95.213.242",
    password:"zzh0117.",
    port:"5433",
    query:"SELECT start_date FROM public.\"000001.XSHE_day_pred\" WHERE step=1 AND model='xgboost_2022-01-01_2023-12-31_1_5' ORDER BY start_date ASC",
    type: "psql",
    user: "postgres"
};
  let date_table = await execQuery(date_config)
  //console.log(date_table)
  
  return date_table
}

get_datelist().then(res=>{
    //console.log(res)  
    const dateStrings = res.data.map(obj => obj['start_date'])  
    //console.log(dateStrings) 
    date_range=ref(dateStrings)
    start_date.value = new Date(date_range.value[0])
  })



function getLocalDateString(date) {
  const offset = date.getTimezoneOffset() * 60000; // 获取本地时区偏移的毫秒数
  const localDate = new Date(date.getTime() - offset); // 根据偏移量调整日期
  return localDate.toISOString().split('T')[0]; // 返回 'YYYY-MM-DD' 格式的日期字符串
}
const checkAllowedDates = (date) => {
      const formattedDate = getLocalDateString(date);
      return !date_range.value.includes(formattedDate);
    };

let dateChange = () =>{
  console.log("date",chooseDate)
  let dateValue= chooseDate.value
  dateString = `${dateValue.getFullYear()}-${String(dateValue.getMonth() + 1).padStart(2, '0')}-${String(dateValue.getDate()).padStart(2, '0')}`;
  console.log(dateString); // 输出格式为 yyyy-MM-dd 的日期字符串
}


mapping={
            "x_orient":["x_orient"],
            "date":["date"]
        }
//加上selectDataset
watch(selectedModel, (val, oldVal) => {
    let model = models.value.filter(model => model.model_name === val)[0]
    //mapping.value = model.model_config.input
    example.value = model.model_config1.example
})
let handleConfig = (arg) => {
    arg.forEach(item => {
        modelConfig.value[item[0]] = item[1]
    })
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
    
    fetchData_table().then(res => {
            tableData.value = res;
        });
        console.log("tabledata",tableData)
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
    newData.x_orient = totalData[i].total_value;

    // 将新对象添加到数组中
    newTable.push(newData);
}

    return newTable
}

let fetchData_table = async () => {
  const metrics_query="SELECT stock, rank FROM public.selection WHERE date='chooseDate' AND strategy='selectedModel' ORDER BY rank ASC"
  const newQuery1_metrics = metrics_query.replace(/chooseDate/g, dateString);
  const newQuery2_metrics =newQuery1_metrics.replace(/selectedModel/g, selectedModel.value);
  const data_metrics = {
    database: "al",
    host: "47.95.213.242",
    password:"zzh0117.",
    port:"5433",
    query:newQuery2_metrics,
    type: "psql",
    user: "postgres"
};
    console.log("query",data_metrics)
  let table = await execQuery(data_metrics)
  console.log("tableData_table",table)
    return table.data
}



</script> 
 
<style scoped>
.border-solid {
    border: solid;
}
.styled-span {

    font-family: Arial;
    font-size: 23px;
    margin-top: 15px;
    color: #263544;

}

.styled-button {
    background-color: #4CAF50;
    color: white;
    font-family: Arial;
    font-size: 30px;
    border: 15px solid #4CAF50; /* 设置边框大小和颜色 */
    margin-top: 15px; /* 向下移动位置 */
}

.module-border-wrap {
  max-width: 1000px;
  padding: 1rem;
  position: relative; 
  top: 1.5vh; /* 调整垂直位置 */
  background: linear-gradient(to right, #e0edfa, #A7BFE8);
  padding: 5px;
}

@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}

.module {
  background: #263544;
  color: white;
  padding: 0.7rem;
  margin-left: 8px;
  font-size: 18px;
  -webkit-text-stroke:0.3px #e0edfa;
}

.blink {
    animation: blink 1s;
    animation-duration: 5s;  
}

.config-list {
    max-width: 555px; /* 设置最大宽度 */
    background-color: #e0edfa; /* 设置背景颜色 */
    padding: 3px; /* 设置内边距 */
}
</style>