<template>
  <div class="w-full h-screen">
      <div class="flex justify-start" style="margin-left: 80px;">
          <div class="module-border-wrap flex items-center" >
              <div class="module" style="margin-left: 6px; width: 80px;">
                  <span class="blink" >选择策略</span>
              </div>
              <el-select v-model="selectedModel" placeholder="算法或策略收益走势">
                  <el-option v-for="val in models" :key="val.id" :value="val.model_name">
                      {{ val.model_name }}
                  </el-option>
              </el-select>
          </div>                     
      </div>
      <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">
          <div class="module-border-wrap">
              <div class="module">
                  要求数据格式：".csv"  上传后可在策略模块查看相应的策略收益，在数据模块查看上传的数据集。
              </div>
          </div>
      </div>
      <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">
          <div class="module-border-wrap">
              <div class="module">
                  样例：
              </div>
          </div>
          <div class="module-border-wrap" style="margin-left: 400px;">
              <div class="module">
                  您上传的数据：
              </div>
          </div>
      </div>
      <!-- 表格添加数据参考链接https://blog.csdn.net/AnnyXSX/article/details/112469095 -->
      <div class="flex justify-start" style="margin-left: 80px; margin-top: 20px;">            
          <div style="width: 35%;padding:10px">
              <table align="center" width="100%" class="table xunw_table_form" border="0">
                  <tbody>
                  <tr>
                      <th colspan="10" class="zxstyle ly">股票名称（股票代码：000001.XSHE）</th>
                  </tr>
                  <tr>
                      <th  class="zxstyle">日期</th>
                      <th  class="zxstyle">开盘价</th>
                      <th  class="zxstyle">收盘价</th>
                      <th  class="zxstyle">最高值</th>
                      <th  class="zxstyle">最低值</th>
                      <th  class="zxstyle">总值</th>
                  </tr>
                  <tr v-for="(item, index) in sjList" :key="item.id">
                      <td align="center" :rowspan="item.kclxspan" :class="{hidden: item.kclxdis}">{{item.kclx}}</td>
                      <td>{{index+1}}</td>
                      <td>{{item.kcdm}}</td>
                      <td>{{item.kcmc}}</td>
                      <td>{{item.xf}}</td>
                      <td>{{item.cjmc}}</td>

                  </tr>
                  </tbody>
              </table>
          </div>
          <div style="width: 35%;padding:10px;margin-left: 150px;">
              <table align="center" width="100%" class="table xunw_table_form" border="0">
                  <tbody>
                      <tr>
                      <th colspan="10" class="zxstyle ly">股票名称（股票代码：000001.XSHE）</th>
                  </tr>
                  <tr>
                      <th  class="zxstyle">日期</th>
                      <th  class="zxstyle">开盘价</th>
                      <th  class="zxstyle">收盘价</th>
                      <th  class="zxstyle">最高值</th>
                      <th  class="zxstyle">最低值</th>
                      <th  class="zxstyle">总值</th>
                  </tr>
                  <tr v-for="(item, index) in sjList" :key="item.id">
                      <td align="center" :rowspan="item.kclxspan" :class="{hidden: item.kclxdis}">{{item.kclx}}</td>
                      <td>{{index+1}}</td>
                      <td>{{item.kcdm}}</td>
                      <td>{{item.kcmc}}</td>
                      <td>{{item.xf}}</td>
                      <td>{{item.cjmc}}</td>

                  </tr>
                  </tbody>
              </table>
          </div>

      </div>
      <el-upload class="upload-demo"
      action="https://jsonplaceholder.typicode.com/posts/"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :before-remove="beforeRemove"
      :on-exceed="handleExceed"
      :file-list="fileList"
      style="margin-left: 80px; margin-top: 200px;">
          <el-button size="medium" type="primary">点击上传</el-button>
          <div slot="tip" class="el-upload__tip">只能上传csv格式的文件</div>
      </el-upload>
      <el-button type="primary" @click="confirmUpload" style="margin-left: 300px; margin-top: -75px;">确认上传</el-button>
      <div class="w-full h-full">
          <el-row :gutter="20" class="w-full h-full">
              <el-col :span="6" class="w-full h-full" v-if="selectedModel">
                  <ConfigList @confirmUpdate="handleConfig" class="border-solid border-2 border-gray-200 h-full"
                      v-if="models.filter(model => model.model_name === selectedModel)[0]"
                      :config="models.filter(model => model.model_name === selectedModel)[0]?.model_config1">
                  </ConfigList>
              </el-col>
              <el-col :span="18" class="w-full h-full">
                  <div class="h-1/3" v-if="example">
                      <dec-chart :ctype="example.type" :dataset="example.dataset" :mapping="example.mapping">
                      </dec-chart>
                  </div>
                  <el-table class="m-4 h-1/3" v-if="selectedDataset"
                      :data="[datasets.filter(item => item.datasetid === selectedDataset)[0]?.example_row]">
                      <el-table-column
                          v-for="(item, idx) in Object.keys(datasets.filter(item => item.datasetid === selectedDataset)[0]?.example_row)"
                          :key="idx" :prop="item" :label="item">
                      </el-table-column>
                  </el-table>
                  <!-- <el-divider /> -->
                  <div class="h-1/3">
                      <div v-if="selectedModel && selectedDataset">
                          <el-select v-for="item in mapping" :placeholder="item.desc" v-model="item.axis" multiple>
                              <el-option
                                  v-for="col in Object.keys(datasets.filter(item => item.datasetid === selectedDataset)[0].example_row)"
                                  :value="col">
                                  {{ col }}
                              </el-option>
                          </el-select>
                      </div>
                  </div>


              </el-col>
          </el-row>
      </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { axios } from '../../api/axios'
import { useBootstrapStore } from '../../stores/counter';
import { ElMessage } from "element-plus";
import ConfigList from '../../components/algorithm/ConfigList.vue'
import DecChart from '../../components/charts/DecChart.vue';
import { saveDataset } from "@/api/sqllab/utils";
import dayjs from "dayjs";
let bootstrap = useBootstrapStore();
let models = ref(bootstrap.bootstrap.models);
let datasets = ref(bootstrap.bootstrap.dataset);
let mapping = ref([])
let modelConfig = ref({});

let selectedModel = ref(null);

let selectedDataset = ref(null)
let example = ref(null)
//加上selectDataset
watch(selectedModel, (val, oldVal) => {
  let model = models.value.filter(model => model.model_name === val)[0]
  mapping.value = model.model_config1.input
  example.value = model.model_config1.example
})
let handleConfig = (arg) => {
  arg.forEach(item => {
      modelConfig.value[item[0]] = item[1]
  })
}

let confirm = () => {
  let formData = new FormData();
  formData.append('model_name', selectedModel.value)
  formData.append('dataset', datasets.value.filter(item => item.datasetid === selectedDataset.value)[0])
  formData.append('mapping', mapping.value)
  formData.append('config', models.value.filter(model => model.model_name === selectedModel.value)[0].model_config1)
  let param = {
      'model_name': selectedModel.value, 'dataset': datasets.value.filter(item => item.datasetid === selectedDataset.value)[0],
      'mapping': mapping.value, 'config': modelConfig.value
  }
  axios({
      //TODO: 不能这么恶心
      url: "http://localhost:8001/train",
      method: "POST",
      data: param
  }).then((res) => {
      let response = res.data
      ElMessage.success({
          message: '操作成功' + ',输出数据集uid为' + response.data.table_name,
          type: 'success'
      });
      return response
  }).then(response => {
      let data = response.data
      data.dataset_name = response.data.table_name;
      let config = {}
      // let timestamp = dayjs().format('YYYY-MM-DD HH:mm:ss')
      // config['dataset_name'] = selectedModel.value.toString()+'_'+selectedDataset.value.toString()
      // +'_output'+timestamp
      data.query = 'select * from ' + data['table_name']
      config['dataset_name'] = data.table_name
      config['query'] = 'select * from ' + data['table_name']
      config['example_row'] = data['example_row']
      config['config'] = data

      saveDataset(config)
  })
  //function读取param
}

//上传文件代码，可能需要修改
let fileList = ref([]);

const handlePreview = async file => {
console.log(file);
};

const handleRemove = (file, fileList) => {
console.log(file, fileList);
};

const beforeRemove = (file, fileList) => {
return window.confirm(`确定移除 ${file.name}？`);
};

const handleExceed = (files, fileList) => {
this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
};

//确认上传部分：
const confirmUpload = () => {
// 执行上传操作，可以在这里调用接口上传文件
console.log("确认上传");
// 可以在这里获取已选择的文件列表 fileList 进行上传操作
// 例如：axios.post('/upload', fileList)
};
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
max-width: 1000px;
padding: 1rem;
position: relative; 
top: 1.5vh; /* 调整垂直位置 */
background: linear-gradient(to right, red, purple);
padding: 3px;
}

.module {
background: #263544;
color: white;
padding: 0.7rem;
}
</style>