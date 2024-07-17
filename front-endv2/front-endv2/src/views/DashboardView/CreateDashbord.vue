<template>
    <div class="w-full h-screen">

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
    // let formData = new FormData();
    // formData.append('model_name', selectedModel.value)
    // formData.append('dataset', datasets.value.filter(item => item.datasetid === selectedDataset.value)[0])
    // formData.append('mapping', mapping.value)
    // formData.append('config', models.value.filter(model => model.model_name === selectedModel.value)[0].model_config)
    // let param = {
    //     'model_name': selectedModel.value, 'dataset': datasets.value.filter(item => item.datasetid === selectedDataset.value)[0],
    //     'mapping': mapping.value, 'config': modelConfig.value
    // }
    // axios({
    //     //TODO: 不能这么恶心
    //     url: "http://localhost:8001/train",
    //     method: "POST",
    //     data: param
    // }).then((res) => {
    //     let response = res.data
    //     ElMessage.success({
    //         message: '操作成功' + ',输出数据集uid为' + response.data.table_name,
    //         type: 'success'
    //     });
    //     return response
    // }).then(response => {
    //     let data = response.data
    //     data.dataset_name = response.data.table_name;
    //     let config = {}
    //     // let timestamp = dayjs().format('YYYY-MM-DD HH:mm:ss')
    //     // config['dataset_name'] = selectedModel.value.toString()+'_'+selectedDataset.value.toString()
    //     // +'_output'+timestamp
    //     data.query = 'select * from ' + data['table_name']
    //     config['dataset_name'] = data.table_name
    //     config['query'] = 'select * from ' + data['table_name']
    //     config['example_row'] = data['example_row']
    //     config['config'] = data

    //     saveDataset(config)
    // })
    //function读取param
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
  background: linear-gradient(to right, red, purple);
  padding: 3px;
}

.module-border-wrap1 {
  max-width: 350px;
  padding: 1rem;
  position: relative;
  left: -850px;
  background: linear-gradient(to right, red, purple);
  padding: 3px;
  display: flex;
  flex-direction: column;
  

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