<template>
  <div class="w-full h-full" style="margin-left: 15px;">
    <div class="flex h-0" >
      <el-steps class="w-full" :active="active" align-center>
        <el-step title="步骤一" description="选择数据集" />
        <el-step title="步骤二" description="选择算法模型" />
      </el-steps>

    </div>
    <div v-if="active === 1">
      <div>
        <my-header content="选择数据集" class="custom-header " ></my-header>
      </div>
      <div class="flex gap-x-4">
        <div class="select_btn">
          <el-select v-if="options" v-model="value" class="m-2" placeholder="Select" size="large" >
            <el-option v-for="item in uniqueDatasets" :key="item" :label="item" :value="item" />
          </el-select>
        </div>
        <div>
          <el-button class="m-3" type="primary" @click="goNext">下一步</el-button>
        </div>
      </div>
      <!--<div v-if="options.filter(item => item.model_name == value)">
        <el-table :data="options.filter(item => item.model_name == value)">
          <el-table-column
            v-for="(item, idx) in Object.keys(options.filter(item => item.model_name == value))" :key="idx"
            :prop="item" :label="item">
          </el-table-column>
        </el-table>
      </div>-->
      <!--<my-header content="图表集合"></my-header>
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
                </el-icon>-->
                <!-- <el-button type="danger" ">delete</el-button> -->
              <!--</div>
            </div>
          </div>
        </div>

      </div>-->


    </div>
    <div v-if="active === 2">
      <my-header content="选择算法模型"></my-header>
      <div class="flex gap-4">
        <div>
          <el-button @click="active = 1">上一步</el-button>
        </div>
        <div>
          <el-button type="primary" @click="confirm">开始绘制</el-button>
        </div>
      </div>
      <div class="m-4"><!--7.4增加多选功能-->
        <el-select v-model="chartValue" class="m-4" multiple>
          <el-option v-for="item in options.filter(item => item.dataset == value)" :key="item.model_name" :label="item.model_name" :value="item.model_name" />
        </el-select>
        <!-- <el-date-picker v-model="chooseDate" type="date" placeholder="选择日期" :picker-options="pickerOptions" @change="dateChange"> 
        </el-date-picker> -->
        <el-date-picker v-model="chooseDate" type="date" placeholder="选择日期" :disabled-date="checkAllowedDates" :defaultValue="start_date" @change="dateChange"> 
        </el-date-picker>

      </div>
    </div>
    <!--7.4增加多选功能-->
    <!-- <div class="h-1/2 border-gray-400 bg-sky-50" style="margin-top: 18px; max-width: 1210px;" >
      <TimeSeries v-if="data && data.length > 0" :formData="data" :chart="'TSL'" ref="chartRef" :mapping="mapping"/>
    </div> -->
    <div class="h-1/2 border-gray-400 bg-sky-50" style="margin-top: 18px; max-width: 1210px;" >
      <MultiLineChart v-if="data && data.length > 0" :formData="data" :chart="'TSL'" ref="chartRef" :mapping="mapping"/>
    </div>

    <div class="mt-4 bg-sky-50" style="width: 97.2%;">
      <el-table :data="tableData" border class="bg-sky-50">
        <el-table-column prop="model_name" label="算法名称"></el-table-column>
        <el-table-column prop="metrics" label="评价指标"></el-table-column>
        <el-table-column prop="value" label="值">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script setup>
import { ref,watch,nextTick} from 'vue'
import { useBootstrapStore } from '../../stores/counter';
import MyHeader from '../../components/trivial/MyHeader.vue'
import { ElMessage,ElDatePicker} from 'element-plus';
import { useRouter } from 'vue-router'
import { deleteChart, getAllChart } from "@/api/chart/chartApi";
import { execQuery } from '@/api/sqllab/utils';
import TimeSeries from '@/components/charts/TimeSeries.vue';
// 7.4增加多选功能
import MultiLineChart from '@/components/charts/MultiLineChart.vue';
import DecChart from "@/components/charts/DecChart.vue";
import { GenNonDuplicateID } from '../../utils/utils';
const router = useRouter()
const bootstrapStore = useBootstrapStore();
let options = ref(bootstrapStore.bootstrap.model_datasets);
console.log("options",options)
let uniqueDatasets = [...new Set(options.value.map(item => item.dataset))];
//需要改：确保每个用户都能看到自己的数据集
console.log("uniqueDatasets",uniqueDatasets)
//let dataset_name=去重
//TODO: // replace chart with real data
let modelOption=ref(['xgboost', 'triformer'])
let chartOption = ref(['TSL', 'LPC', 'Table','SLC'])
let chartValue = ref([])
let value = ref(null);
let active = ref(1)
let charts = ref([])
let data = ref([])
let mapping = ref([])
let datasetName= ref([])
let modelName=ref([])
let chooseDate=ref([])
let dateString=ref([])
let tableData=ref([])
let date_range = ref([]) 
const start_date = ref(null);
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
    console.log(dateStrings) 
    date_range=ref(dateStrings)
    start_date.value = new Date(date_range.value[0])
    //date_range=res.value
    //console.log("date_rangenew",date_range) 
    //dateList.value=dateStrings;
  })
//let date_range=ref([])
//console.log("date_range",date_range)



function getLocalDateString(date) {
  const offset = date.getTimezoneOffset() * 60000; // 获取本地时区偏移的毫秒数
  const localDate = new Date(date.getTime() - offset); // 根据偏移量调整日期
  return localDate.toISOString().split('T')[0]; // 返回 'YYYY-MM-DD' 格式的日期字符串
}
const checkAllowedDates = (date) => {
      const formattedDate = getLocalDateString(date);
      return !date_range.value.includes(formattedDate);
    };


const chartRef = ref();
// watch(data, (newData, oldData) => {
//   // 更新 formData
//   data.value = newData;
//   console.log("newData",newData)
//   // 当数据变化时，通过 $refs 获取图表组件的引用，并调用更新方法
//   // // if (newData !== oldData) {
//   // //       nextTick(() => {
//   // //         // 更新图表组件
//   // //         if (chartRef.value) {
//   // //           chartRef.value.updateChart(newData);
//   // //         }
//   // //       });
//   //     }
// });
const pickerOptions = ref({
  disabledDate:(time) =>{
    // 设置开始日期为 2015-01-15
    const startDate = new Date('2015-01-15');
    // 设置结束日期为 2016-01-04
    const endDate = new Date('2016-01-04');
    //return time.getTime() < Date.now() - 8.64e7; // 示例：禁用过去的日期
    // 设定日期范围
    return time.getTime() < startDate.getTime() || time.getTime() > endDate.getTime();
  }
});

// mapping={
//             "X_predict":["pred"],
//             "X":["real"],
//             "date":["date"]
//         }
mapping={
            "X_predict1":["pred"],
            "X":["real"],
            "date":["date"]
        }
//console.log("2221",data)
let dateChange = () =>{
  console.log("date",chooseDate)
  let dateValue= chooseDate.value
  dateString = `${dateValue.getFullYear()}-${String(dateValue.getMonth() + 1).padStart(2, '0')}-${String(dateValue.getDate()).padStart(2, '0')}`;
  //console.log(dateString); // 输出格式为 yyyy-MM-dd 的日期字符串
}
getAllChart().then(res => {
  charts.value = res.data.data
})
let goNext = () => {
  if (value.value) {
    active.value = 2
    datasetName = value.value.toString()
  } else {
    ElMessage.error('Please choose a dataset')
  }
  
}
let confirm = () => {
  if (chartRef.value){
    setTimeout(() => {
      chartRef.value.refreshData()
    }, 500);

  }
 
  modelName=chartValue.value.toString()
  fetchData_liner().then(res => {
            data.value = res;
        });
        console.log("data",data)
  fetchData_table().then(res => {
            tableData.value = res;
        });
        console.log("tabledata",tableData)

}
//7.4添加多选功能
let fetchData_liner = async () => {
  //取pred值
  let allData = [];
  console.log("modelName",modelName)
  const modelNames = modelName.split(',');
  // 创建一个空数组用于存储合并后的数据
  
  for (const singlemodelName of modelNames)
  {
    const data_pred = {
      database: "al",
      host: "47.95.213.242",
      password:"zzh0117.",
      port:"5433",
      query:"SELECT * FROM public.\"datasetName_day_pred\" WHERE \"start_date\"='DATE' AND \"model\"='modelName' ORDER BY step ASC LIMIT 5",
      type: "psql",
      user: "postgres"
      };
    const newQuery1_pred = data_pred.query.replace('datasetName', datasetName);
    const newQuery2_pred = newQuery1_pred.replace('modelName', singlemodelName);
    const newQuery3_pred = newQuery2_pred.replace('DATE', dateString);
    const newData_pred = {
      database: "al",
      host: "47.95.213.242",
      password:"zzh0117.",
      port:"5433",
      query:newQuery3_pred,
      type: "psql",
      user: "postgres"
    }
    console.log("pred_config",newData_pred)
    let pred_table = await execQuery(newData_pred)
    console.log("pred",pred_table.data)

    //取history值
    //const data_history_query="SELECT \"time\",\"close\" FROM public.history WHERE \"code\"='datasetName'ORDER BY TO_DATE(\"time\", 'YYYY-MM-DD') ASC LIMIT 489",
    const data_history_query="(SELECT * FROM (SELECT * FROM public.history WHERE \"code\" = 'datasetName' AND \"time\" < 'dateString' ORDER BY \"time\" DESC  LIMIT 25) AS before_specified_date ORDER BY \"time\" ASC) UNION ALL(SELECT * FROM public.history WHERE \"code\" = 'datasetName' AND \"time\" = 'dateString')UNION ALL(SELECT * FROM (SELECT * FROM public.history WHERE \"code\" = 'datasetName' AND \"time\" > 'dateString' ORDER BY \"time\" ASC LIMIT 4) AS after_specified_date ORDER BY \"time\" ASC);"
    const newQuery1_history = data_history_query.replace(/datasetName/g, datasetName);
    const newQuery2_history =newQuery1_history.replace(/dateString/g, dateString);
    const newData_history = {
      database: "al",
      host: "47.95.213.242",
      password:"zzh0117.",
      port:"5433",
      query:newQuery2_history,
      type: "psql",
      user: "postgres"
    }
    let history_table = await execQuery(newData_history)
    // console.log("history",history_table.data)
    const historyData = history_table.data;
    const predData = pred_table.data;
    let newTable = [];
    // 合并数据
    for (let i = 0; i < historyData.length; i++) 
    {
      let newData = {};

      // 设置日期属性
      newData.date = historyData[i].time;

      // 设置实际值属性
      newData.real = historyData[i].close;

      // 设置预测值属性
      if(i>=historyData.length-predData.length){
        newData.pred = (predData[i-(historyData.length-predData.length)].pred_return+1)*historyData[i-1].close;
      }
      else{
        newData.pred=null
      }
      // 将新对象添加到数组中
      newTable.push(newData);
    }
    allData.push({
          modelName: singlemodelName,
          data: newTable
        });
  }
console.log("allData",allData);
    return allData
}
let fetchData_table = async () => {
  const modelNames = modelName.split(',');
  let multiTableData = [];
  for (const singlemodelName of modelNames)
  {
    const metrics_query="SELECT model_name, metrics, ROUND(value, 6) AS value FROM public.metrics_day_pred WHERE stock='datasetName' AND model_name='modelName'"
    const newQuery1_metrics = metrics_query.replace(/datasetName/g, datasetName);
    const newQuery2_metrics =newQuery1_metrics.replace(/modelName/g, singlemodelName);
    const data_metrics = {
      database: "al",
      host: "47.95.213.242",
      password:"zzh0117.",
      port:"5433",
      query:newQuery2_metrics,
      type: "psql",
      user: "postgres"
  };
    let table = await execQuery(data_metrics)
    console.log("table",table.data)
    multiTableData.push(table.data)

  }
  console.log("multiTableData",multiTableData)
  const mergedArray = multiTableData.reduce((acc, curr) => acc.concat(curr), []);
  return mergedArray
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

<style scoped>

.module {
  background: #263544;
  color: white;
  padding: 0.7rem;
  margin-left: 8px;
  font-size: 18px;
  -webkit-text-stroke:0.3px #e0edfa;
}



</style>