<template>
    <div class="w-full h-screen">
        <div class="flex justify-evenly">
            <div class="styled-span">
                <span>
                    选择模型
                </span>
                <el-select v-model="selectedModel">
                    <el-option v-for="val in models" :key="val.id" :value="val.model_name">
                        {{ val.model_name }}
                    </el-option>
                </el-select>
            </div>

            <div class="styled-span">
                <span>
                    选择数据集
                </span>
                <el-select v-model="selectedDataset">
                    <el-option v-for="(val, idx) in datasets" :key="idx + 2324" :label="val.dataset_name"
                        :value="val.datasetid">
                        {{ val.dataset_name }}
                    </el-option>
                </el-select>
            </div>
            
        </div>
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
</style>