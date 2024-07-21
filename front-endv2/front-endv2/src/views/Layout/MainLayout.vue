<template>
    <div class="w-full h-full">
        <el-container class="w-full h-full">
            <el-header class=" bg-#88888-900 text-white" style="height: 90px; display: flex; justify-content: center;">
                <div class="w-full h-full flex items-center justify-between" style="background-color: #263544;">                   
                    <img src="./logoko1.png" alt="ECNU-Tech Logo" style="width: 130px; margin-left: 1px;margin-top: 20px;">
                    <div class="text-4xl font-bold" style="display: flex; justify-content: center; align-items: center; flex: 1;">
                        算法可视化平台
                    </div>
                    <div style="margin-right: 10px;">
                        <!-- 根据用户登录状态显示不同内容 -->                      
                        <template v-if="$store.state.isLoggedIn">
                            
                            <div class="logged-in-info">
                              <span class="logged-in-text">Hi! {{ $store.state.username }} <el-icon style="margin-left: 2px;"><User /></el-icon></span>                      
                              <el-button type="text" @click="goToLogout" class="btn three">退出</el-button>
                            </div>
                        </template>
                        <template v-else>
                            <el-button type="text" @click="goToLoginOrRegister"  class="btn one">登录/注册</el-button>
                        </template>
                    </div>
                </div>
            </el-header>

            <el-container class="w-full h-full" style="background-color: blue;">
                <div>

                    <el-menu :collapse="collapse" class=" h-screen overflow-hidden" :default-active="defaultActivate"
                        router>
                        <div class="h-10 border-b-2 flex border-gray-100 items-center" style="width: 100%; height: 100px; background-color: #263544">
                            <!--删除了服务模块的代码-->
                            <div @click="collapse = !collapse">
                                <el-icon class="mt-2 m-auto text-2xl pl-5 text-zinc-600 cursor-pointer">
                                    <Operation />
                                </el-icon>
                            </div>
                        </div>
                        <el-divider class="m-0 p-0" />
                        
                        <el-menu-item :route="{ name: 'newChartView' }" index="1" style="font-size: 20px;">
                            <el-icon>
                                <document />
                            </el-icon>
                            <span style="text-align: center;">算法模块</span>
                        </el-menu-item>
                        
                        <el-menu-item :route="{ name: 'algorithms' }" index="2" style="font-size: 20px;">
                            <el-icon>
                                <location />
                            </el-icon>
                            <span>策略模块</span>
                        </el-menu-item>
                        
                        <el-menu-item :route="{ name: 'datasourceLayout' }" index="3"  style="font-size: 20px;">
                            <el-icon>
                                <document />
                            </el-icon>
                            <span>数据模块</span>
                        </el-menu-item>
                        
                        <el-menu-item index="4" :route="{ name: 'dashboard' }" style="font-size: 20px;">
                            <el-icon>
                                <setting />
                            </el-icon>
                            <span>因子分析</span>
                        </el-menu-item>
                        <el-menu-item index="5" :route="{ name: 'dashboardList' }" style="font-size: 20px;">
                            <el-icon>
                                <setting />
                            </el-icon>
                            <span>上传数据</span>
                        </el-menu-item>
                    </el-menu>
                </div>

                <el-main class="bg">
                    <RouterView></RouterView>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script setup>
import { RouterView, useRoute } from 'vue-router';
import { ref} from "vue";
import { onMounted } from 'vue'


// let defaultActivate = ref('0')
let defaultActivate = ref('1')

let dropdownMenu = ref(null)
let collapse = ref(false)
let pathNameMapping = [
    { name: 'newChartView', index: '1' },
    { name: 'algorithms', index: '2' },
    
    // { name: 'chooseView', index: '3' },
    { name: 'datasourceLayout', index: '3' },
    { name: 'dashboard', index: '4' },
    { name: 'dashboardList', index: '5' },
]
const route = useRoute()

// 
console.log(defaultActivate)
pathNameMapping.forEach(item => {
    if (item.name === route.name) {
        defaultActivate.value = item.index
        
    }
})
// onMounted(() => {
//       pathNameMapping.forEach(item => {
//         if (item.name === route.name) {
//           defaultActivate.value = item.index
//           
//         }
//       })
//     })



</script>

<script>

export default {
    methods:{
      async goToLoginOrRegister() {
        this.$router.push({ name: 'login' });
      },
      async goToLogout() {
        this.$store.commit('setLoggedIn', false);
        this.$store.commit('setUsername', '');
        this.$router.push({ name: 'home' });
      }
    }
}

</script>

<style scoped>


.el-header {
    background-color: #263544; /* 灰色 */
    width: 100%; /* 拉长宽度 */
    height: 80px; /* 设置高度 */
    padding: 0 20px; /* 添加 padding */
}

.el-menu {
    background-color: #263544;
    color: #B7C0CD;

}

.el-menu-item {
    display: flex;
    align-items: center;
    padding: 30px;
    margin-top: 5px; /* 上间距 */
    margin-bottom: 5px; /* 下间距 */

}
.el-menu-item .el-icon {
    margin-right: 10px; /* 调整图标和文字之间的间距 */
}

/*  */
/* 菜单项激活状态样式 */
.el-menu-item:not(.is-active) {
    background-color: #263544;
    color: #B7C0CD;
}

.el-menu-item.is-active {
    background-color: #13133286;
    color: #42a5f5;
}

/* 用户菜单下拉项样式 */
.el-dropdown-menu__item {
    font-size: 14px;
    color: #666;
}

/* 主要内容区域边距和背景色 */
.el-main {
    padding: 10px;
    background-color: #9ea8b5;
    transition: background-color 0.3s; /* 添加颜色过渡效果 */
}

.el-main:hover {
    background-color:  hsla(215, 30%, 83%, 0.922); /* 悬停时的背景颜色 */
}


.btn {
  border: 1px solid;
  background-color: transparent;
  text-transform: uppercase;
  font-size: 14px;
  padding: 10px 20px;
  font-weight: bold;
}

.one {
  color: #4cc9f0;
}

.btn:hover {
  color: white;
  border: 0;
}

.one:hover {
  background-color: #4cc9f0;
  -webkit-box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
  -moz-box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
  box-shadow: 10px 10px 99px 6px rgba(76,201,240,1);
}

.three {
  color: #b9e769;
}

.three:hover {
  background-color: #b9e769;
  -webkit-box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
  -moz-box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
  box-shadow: 10px 10px 99px 6px rgba(185, 231, 105, 1);
}

.logged-in-info {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}

.logged-in-text {
    margin-bottom: 8px; /* Adjust as needed for spacing */
    font-weight: bold;
    font-size: 16px; /* Example of custom styling */

}

</style>