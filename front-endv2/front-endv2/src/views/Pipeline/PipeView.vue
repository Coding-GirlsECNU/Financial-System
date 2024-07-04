<script setup>
import { ref,watch } from 'vue';
import Editor from '@/components/sqllab/Editor.vue';
let data = ref(JSON.stringify({
    total: 25,
    limit: 10,
    skip: 0
}));
let task = ref([
    'all_detect_label_config',
    'all_detect_score_config',
    'fixed_detect_label_config',
    'fixed_detect_score_config',
    'fixed_forecast_config',
    'rolling_forecast_config',
    'unfixed_detect_label_config',
    'unfixed_detect_score_config'
])
let selectedTask = ref('')
watch(selectedTask,(val,oldVal)=>{
    if(val!==''){
        
    }
})
</script>
<template>
    <div class="w-full h-full">
        <div class="w-full h-20">
            <div class="m-2">
                <span>Task</span>
                <el-select class="ml-2" v-model="selectedTask">
                    <el-option v-for="item in task" :label="item" :value="item">
                    </el-option>
                </el-select>
            </div>
        </div>
        <div class=" w-full h-52">
            <Editor class="w-full h-full" cid="editor" v-model="data" lang="json" :showDiff="false" />
        </div>

    </div>
</template>