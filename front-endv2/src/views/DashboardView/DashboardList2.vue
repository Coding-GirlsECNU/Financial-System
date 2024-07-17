<template>
  <div class="w-full h-full">
    <div class="w-full h-full grid grid-cols-4 gap-8">
      <div v-for="item in dashboard">
        <el-card class="space-y-3 m-3">
          <div>
            {{ item.dashboard_name }}
          </div>
          <div class="mt-3">
            <el-button type="primary"
              @click="() => { jumpTo('dashboardView', { 'config': JSON.stringify(item) }) }">查看</el-button>
            <el-button type="danger" @click="() => { handleDelete(item) }">delete</el-button>
          </div>
        </el-card>
      </div>

    </div>
  </div>
</template>
<script setup>
import { useBootstrapStore } from "@/stores/counter";
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { deleteBoard } from "@/api/dashboard/dashboardApi";
import { ElMessage } from "element-plus";
let router = useRouter()
let bootstrap = useBootstrapStore()
let dashboard = ref(bootstrap.bootstrap.dashboard)

const jumpTo = (name, query) => {
  router.push({
    name: name,
    query: query,
  })
}
const handleDelete = (board) => {
  deleteBoard(board).then(res => {
    let response = res.data;
    dashboard.value = response.data;
    if (response.code === 200) {
      ElMessage.success('删除成功')
    } else {
      ElMessage.error('删除失败')
    }
  }).then(() => {
    bootstrap.bootstrap.dashboard = dashboard.value
  })
}
</script>