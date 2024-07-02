<template>
    <div class="w-full h-full">
        <el-container class="w-full h-full">
            <el-header class=" bg-gray-900 text-white" style="height: 70px; display: flex; justify-content: center;">
                <div class="w-full h-full flex flex-col items-center">
                    <div class="pt-3 text-4xl font-bold">
                        算法可视化平台
                    </div>
                    <div class="pt-3">

                    </div>
                </div>
            </el-header>

            <el-container class="w-full h-full" style="background-color: blue;">
                <div>

                    <el-menu :collapse="collapse" class=" h-screen overflow-hidden" :default-active="defaultActivate"
                        router>
                        <div class="h-10 border-b-2 flex border-gray-100 items-center" style="width: 100%;">
                            <div class="flex-1 text-center m-auto" v-if="!collapse" style="font-size: 25px;color:white;background-color: #5cadff; border-radius: 10px;">
                                服务管理
                            </div>
                            <div @click="collapse = !collapse">
                                <el-icon class="mt-2 m-auto text-2xl pl-5 text-zinc-600 cursor-pointer">
                                    <Operation />
                                </el-icon>
                            </div>
                        </div>
                        <el-divider class="m-0 p-0" />

                        <el-menu-item :route="{ name: 'algorithms' }" index="1" style="font-size: 20px;">
                            <el-icon>
                                <location />
                            </el-icon>
                            <span>算法模块</span>
                        </el-menu-item>
                        <el-menu-item :route="{ name: 'datasourceLayout' }" index="2"  style="font-size: 20px;">
                            <el-icon>
                                <document />
                            </el-icon>
                            <span>数据源模块</span>
                        </el-menu-item>
                        <el-menu-item :route="{ name: 'newChartView' }" index="3" style="font-size: 20px;">
                            <el-icon>
                                <document />
                            </el-icon>
                            <span>图表模块</span>
                        </el-menu-item>
                        <el-menu-item index="4" :route="{ name: 'dashboard' }" style="font-size: 20px;">
                            <el-icon>
                                <setting />
                            </el-icon>
                            <span>大屏模块</span>
                        </el-menu-item>
                        <el-menu-item index="5" :route="{ name: 'dashboardList' }" style="font-size: 20px;">
                            <el-icon>
                                <setting />
                            </el-icon>
                            <span>大屏集合</span>
                        </el-menu-item>
                    </el-menu>
                </div>

                <el-main class="bg-white">
                    <RouterView></RouterView>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup>
import { RouterView, useRoute } from 'vue-router';
import { ref } from "vue";

let defaultActivate = ref('1')
let dropdownMenu = ref(null)
let collapse = ref(false)
let pathNameMapping = [
    { name: 'algorithms', index: '1' },
    { name: 'newChartView', index: '3' },
    { name: 'chooseView', index: '3' },
    { name: 'datasourceLayout', index: '2' },
    { name: 'dashboard', index: '4' },
    { name: 'dashboardList', index: '5' },
]
const route = useRoute()
pathNameMapping.forEach(item => {
    if (item.name === route.name) {
        defaultActivate.value = item.index
    }
})

</script>

<style scoped>


.el-header {
    background-color: #515a6e; /* 灰色 */
    width: 100%; /* 拉长宽度 */
    height: 80px; /* 设置高度 */
    padding: 0 20px; /* 添加 padding */
}

/* 菜单项激活状态样式 */
.el-menu-item.is-active {
    background-color: #F3F4F6;
    color: #333;
}

/* 用户菜单下拉项样式 */
.el-dropdown-menu__item {
    font-size: 14px;
    color: #666;
}

/* 主要内容区域边距和背景色 */
.el-main {
    padding: 10px;
    background-color: blue;
}


</style>