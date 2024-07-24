<template>
    <div class="w-full h-screen">
        <div class="flex justify-start" style="margin-left: 80px;">
            <div class="flex items-center">
                <div class="module" style="margin-left: 6px; width: 80px;">
                    <span class="blink">选择股票</span>
                </div>
                <el-select v-model="selectDataset" placeholder="请首先选择你要预测的股票" >
                    <!-- <el-option v-for="val in models" :key="val.id" :value="val.model_name">
                        {{ val.model_name }} -->
                    <el-option v-for="item in uniqueDatasets" :key="item" :label="item" :value="item" />
                    <!-- </el-option> -->
                </el-select>
            </div>
        </div>
        <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">
            <div >
                <div class="module">
                    要求数据格式：".csv" 上传后可在策略模块查看相应的策略收益，在数据模块查看上传的数据集。
                </div>
            </div>
        </div>

        <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">
            <div>
                <div class="module">样例：</div>
            </div>          
            <div style="margin-left: 480px;">
                <div class="module">您上传的数据： </div>
                <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">
                    <div style="width: 80%;padding:10px">
                        <table align="center" width="100%" class="table xunw_table_form" border="0">
                            <tbody>
                                <!-- <tr>
                                    <th v-for="(value, key) in uploadedData[0]" :key="key" class="zxstyle">{{ key }}</th>
                                </tr>
                                <tr v-for="(item, index) in uploadedData" :key="index">
                                    <td v-for="(value, key) in item" :key="key">{{ value }}</td>
                                </tr> -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <!-- <div class="flex justify-start" style="width: 32%; margin-top: 5px; margin-left: 100px;">
          <el-table :data="tableData" border>
            <el-table-column prop="start_date" label="Start Date"></el-table-column>
            <el-table-column prop="model" label="Model"></el-table-column>
            <el-table-column prop="step" label="Step"></el-table-column>
            <el-table-column prop="pred_return" label="Predicted Return"></el-table-column>
          </el-table>

        </div>  -->
        <el-row :gutter="80" class="table-container" style="width: 85%; margin-left: 80px; margin-top: 20px;">
          <el-col :span="12">
            <el-table :data="tableData" border>
              <el-table-column prop="start_date" label="Start Date"></el-table-column>
              <el-table-column prop="model" label="Model" width="80px"></el-table-column>
              <el-table-column prop="step" label="Step" width="60px"></el-table-column>
              <el-table-column prop="pred_return" label="Predicted Return"></el-table-column>
            </el-table>
          </el-col>

          <el-col :span="12">
            <el-table :data="uploadedData" border>
              <el-table-column v-for="(value, key) in uploadedData[0]" :key="key" :prop="key" :label="key"></el-table-column>
            </el-table>
          </el-col>
        </el-row>

        <el-upload 
            :before-upload="handleUpload"
            :on-preview="handlePreview"
            :on-exceed="handleExceed"
            :file-list="fileList"
            accept=".csv"
            style="margin-left: 80px; margin-top: 200px;">
            <el-button size="medium" type="primary" class="custom-button">点击上传</el-button>   
            <div class="typing">只能上传csv格式的文件</div>  
            
        </el-upload>
        
    </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: [
        { start_date: '2023-01-01', model: 'Model1', step: 1, pred_return: 0.05 },
        { start_date: '2023-01-02', model: 'Model2', step: 2, pred_return: 0.06 }
      ]
    };
  },
};
</script>

<script setup>
import Papa from 'papaparse';
import { ref, watch } from 'vue';
import { axios } from '../../api/axios';
import { useBootstrapStore } from '../../stores/counter';
import { ElMessage } from "element-plus";
import ConfigList from '../../components/algorithm/ConfigList.vue';
import DecChart from '../../components/charts/DecChart.vue';
import { saveDataset, execInsert, execQuery } from "@/api/sqllab/utils";
import dayjs from "dayjs";
import { useStore } from 'vuex';
const bootstrapStore = useBootstrapStore();
let options = ref(bootstrapStore.bootstrap.model_datasets);
let uniqueDatasets = [...new Set(options.value.map(item => item.dataset))];
const selected_dataset = ref(null);
const uploadedData = ref([]);
const bootstrap = useBootstrapStore();
const models = ref(bootstrap.bootstrap.models);
const datasets = ref(bootstrap.bootstrap.dataset);
const mapping = ref([]);
const modelConfig = ref({});
const store = useStore();
const selectDataset = ref(null);
const chosenDataset = ref(null); // 用于记录选择的变量
const example = ref(null);
const fileList = ref([]);
const parsedData = ref(null);
const dbConfig = {
    database: 'al',
    host: '47.95.213.242',
    password: 'zzh0117.',
    port: '5433',
    type: 'psql',
    user: 'postgres'
};
let query = ref([]);
// console.log("asdddd11111111111",this.$store.state.username);

//每当用户选择了一个要预测的股票，就修改chosenDataset的值
watch(selectDataset, (newValue) => {
    if (newValue) {
        chosenDataset.value = newValue;
        console.log(chosenDataset);
        ElMessage.success(`选择了股票: ${newValue}`);
        // 可以在这里执行其他逻辑，例如调用API或者更新其他状态
    }
});

const handleConfig = (arg) => {
    arg.forEach(item => {
        modelConfig.value[item[0]] = item[1];
    });
};

const handleUpload = (file) => {
    const reader = new FileReader();
    reader.onload = (event) => {
        const csvData = event.target.result;
        const parsed = Papa.parse(csvData, { header: true, dynamicTyping: true }).data;
        parsedData.value = parsed;
        confirmUpload();
    };
    reader.onerror = (error) => {
        console.error('读取文件时出错:', error);
    };
    reader.readAsText(file);
};

//确认上传后解析数据并保存到数据库
const confirmUpload = () => {
    if (chosenDataset.value == null) {
        ElMessage.error('请先选择一只股票');
        return ;
    }
    if (parsedData.value) {
        saveToDatabase(parsedData.value);
    } else {
        console.error('没有解析的数据');
    }
};

//执行query
const getQuery = async (query) => {
            try {
                const newDataHistory = { ...dbConfig, query };
                console.log("dao getquery");
                let new_history_data = await execInsert(newDataHistory);
                console.log("success", new_history_data.data.success);
                if (new_history_data.data.success == false )
                {
                    ElMessage.error('保存到数据库时出错，请检查数据格式');
                    return new_history_data;
                }
                ElMessage.success('数据已成功保存到数据库');
                return new_history_data;
            } catch (error) {
                console.error('保存到数据库时出错:', error);
                ElMessage.error('保存到数据库时出错，上传失败！');
            }
        };

const saveToDatabase = async (data) => {
            try {
                console.log("begin to saveToDatabase了！", data);

                //获取用户上传的模型名称
                const modelValues = data.map(row => row.model);
                console.log('Model Values:', modelValues[0]);

                //删除空白的数据行
                const isRowBlank = (row) => {
                    for (const key in row) {
                        if (row.hasOwnProperty(key) && row[key] !== null && row[key] !== undefined && row[key] !== '') {
                            return false;
                        }
                    }
                    return true;
                };

                data = data.filter(row => !isRowBlank(row));

                console.log("asdddd11111111111", store.state.username);

                //将csv文件的行和列格式化成一个query语句
                const columns = [...Object.keys(data[0])].join(', ');
                const values = data.map(row => {  
                    const rowValuesWithUserId = [...Object.values(row)];
                    const rowValues = rowValuesWithUserId.map(value =>
                        typeof value === 'string' ? `'${value.replace(/'/g, "''")}'` : value
                    );
                    return `(${rowValues.join(', ')})`;
                }).join(', ').replace(/,\s*\(\s*\)$/, '');

                const query = `INSERT INTO "${chosenDataset.value}_day_pred" (${columns}) VALUES ${values};`;
                const newDataHistory = { ...dbConfig, query };
                console.log("newData_history", newDataHistory);
                
                let history = await getQuery(query);
                
                console.log("dateStrings", history);

                //将用户新上传的模型存入model_dataset表
                const query2 = `INSERT INTO model_dataset (model_name, dataset) VALUES ('${modelValues[0]}', '${chosenDataset.value}');`;
                const newDataHistory2 = { ...dbConfig, query2 };
                console.log("newData_history", newDataHistory2);
                
                const history2 = await getQuery(query2);
                console.log("dateStrings", history2);
                
                // 在页面展示用户上传的数据
                if (history.data.success == true && history2.data.success == true)
                {
                    uploadedData.value = data.slice(0, 5); // 只显示前5行
                }

            } catch (error) {
                console.error('保存到数据库时出错:', error);
                ElMessage.error('上传失败！');
            }
        };

const handlePreview = (file) => {
    console.log('预览文件:', file);
};

const handleExceed = (files) => {
    ElMessage.warning(`当前限制选择 1 个文件，您选择了 ${files.length} 个文件`);
};



</script>



 
<style scoped>

::v-deep .el-table__body-wrapper .el-table__row {
  background-color: #c8ebfa;
  color: black;
  
}
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



.module {
  background: #263544;
  color: white;
  padding: 0.7rem;
}

#circle-btn { 
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.btn-container {
  position: relative;  
}

.custom-button.el-button {
  border: 0;
  border-radius: 50px;
  color: white;
  background: #5f55af;
  padding: 15px 20px 16px 25px;
  text-transform: uppercase;
  background: linear-gradient(to right, #f72585 50%, #5f55af 50%);
  background-size: 200% 100%;
  background-position: right bottom;
  transition:all 2s ease;
  font-family: 'Microsoft YaHei', sans-serif; /* 使用微软雅黑字体 */
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}


.custom-button.el-button:hover {
   background-position: left bottom;
}

.typing {
	color: rgb(149, 66, 250);
	font-size: 0.9em;
    font-weight: 900;
	width: 21em;
	height: 1.5em;
	border-right: 1px solid transparent;
	animation: typing 2s steps(42, end), blink-caret .75s step-end infinite;
	font-family: Consolas, Monaco;
	word-break: break-all;
	overflow: hidden;
    margin-left: 10px
}
/* 打印效果 */
@keyframes typing {
	from {
		width: 0;
	}

	to {
		width: 21em;
	}
}

/* 光标 */
@keyframes blink-caret {

	from,
	to {
		border-color: transparent;
	}

	50% {
		border-color: currentColor;
	}
}


</style>