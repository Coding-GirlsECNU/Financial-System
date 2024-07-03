<template>
  <div class="w-full h-full">
    <div class="w-full flex justify-start">
      <!-- <div>
        <el-input v-model="name" palceholder="输入查询的数据源信息">
        </el-input>
      </div>
      <div>
        <el-button type="primary">搜索</el-button>
      </div> -->
      <div>
        <el-button type="primary" @click="addNewModal = true">添加</el-button>
      </div>
    </div>
    <div>
      <el-table v-if="datasource" :data="datasource" class="mt-5">
        <el-table-column label="host" prop="config.host"></el-table-column>
        <el-table-column label="port" prop="config.port"></el-table-column>
        <el-table-column label="user" prop="config.user"></el-table-column>
        <el-table-column label="type" prop="config.type"></el-table-column>
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button link type="primary" size="small" @click.prevent="createDataset(scope.$index, scope.row)">
              创建数据源
            </el-button>
            <el-button link type="primary" size="small" @click.prevent="deleteDatasource(scope.$index, scope.row)">
              删除数据源
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <el-dialog class="h-2/3" v-model="addNewModal">
      <el-form label-width="100">
        <el-form-item label="host">
          <el-input v-model="newData.host"></el-input>
        </el-form-item>
        <el-form-item label="port">
          <el-input v-model="newData.port"></el-input>
        </el-form-item>
        <el-form-item label="user">
          <el-input v-model="newData.user"></el-input>
        </el-form-item>
        <el-form-item label="password">
          <el-input v-model="newData.password"></el-input>
        </el-form-item>
        <el-form-item label="type">
          <el-input v-model="newData.type"></el-input>
        </el-form-item>
        <el-form-item label="database">
          <el-input v-model="newData.database"></el-input>
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="float-right">
          <el-button type="primary" @click="() => { addConfirm() }">
            确定
          </el-button>
        </div>
      </template>

    </el-dialog>

  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { useBootstrapStore } from '../../stores/counter';
import { deleteDataSrc, saveDataSrc } from "@/api/datasource/datasrcApi";
import { ElMessage } from "element-plus";

const bootstrapStore = useBootstrapStore();
const router = useRouter()
let datasource = ref(bootstrapStore.bootstrap.datasource);
//TODO:// dialog 可以抽离成 一个组件的形式
let addNewModal = ref(false)
let newData = ref({
  host: '',
  port: '',
  user: '',
  password: '',
  type: '',
  database: ''
})
const addConfirm = () => {
  addNewModal.value = false
  let payload = {
    config: {
      host: newData.value.host,
      port: newData.value.port,
      user: newData.value.user,
      password: newData.value.password,
      type: newData.value.type,
      database: newData.value.database
    }
  }
  saveDataSrc(payload).then(res => {
    let response = res.data;
    if (response.code === 200) {
      ElMessage.success('success')
      datasource.value.push(payload)
    } else {
      ElMessage.error('error')
    }
    addNewModal.value = false

  })

}
let name = ref('')
let createDataset = (idx, row) => {
  let config = row.config
  // convert config to URL search
  let query = "?" + new URLSearchParams(config)
  router.push({ name: 'sqlLab', query: config })
}
let deleteDatasource = (idx, row) => {
  deleteDataSrc(row.datasourceid).then(res => {
    let response = res.data;
    if (response.code === 200) {
      ElMessage.success('success')
      datasource.value.splice(idx, 1)
    } else {
      ElMessage.error('error')
    }
  })
}
</script>

<style scoped></style>
