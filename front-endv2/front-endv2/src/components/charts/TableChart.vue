<template>
    <div :id="props.cid" class="h-full w-full">
        <el-table border  class="w-full h-full" :data="formData">
            <el-table-column v-for="col in cols" :prop="col" :label="col">
            </el-table-column>
        </el-table>

    </div>
</template>
 
<script setup>
import { ref } from 'vue'
const props = defineProps({
    cid: {
        type: String,
        default: ""
    },
    formData: {
        type: Array,
        default: []
    },
    mapping: {
        type: Object,
        default: {}
    }
})
let data = ref([])
let cols = ref(props.mapping.columns)

const refreshData = () => {
    data.value = props.formData
}
const resizeWindow = () => {
    console.log('resize')
}
defineExpose({
    refreshData,
    resizeWindow
})
</script> 
 
<style scoped></style>