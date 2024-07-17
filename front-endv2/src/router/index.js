// import { createRouter, createWebHistory } from 'vue-router'
// import { DashboardView } from '../views/DashboardView/DashboardView'
// const router = createRouter({
//     history: createWebHistory(import.meta.env.BASE_URL),
//     routes: [
//         {
//             path: '/',
//             name: 'home',
//             // path: 'chart', component: () => import('../views/ChartView/NewChartView.vue'), name: 'newChartView',
//             //比如你做了一个主页，要把component给写进去，我猜的哈，我印象里是这样的。然后下面的是子页面，比如
//             // 比如你现在的网页是  sys   然后点击子页面  网页就会变成 sys/choose   子页面还有子页面，比如这里chosse下面还有两个
//             // 一个是chooseView   就hi变成  sys/choose/chooseView  只是这个功能还没实现，点击下一步他没反应   因为你没有给选项。
//             // 我也不知道为什么不行。  可能和你刚才那个上面 port有关，这个我也不懂。
//             redirect: '/sys'
//         },
//         {
//             path: '/sys',
//             name: 'system',
//             // route level code-splitting
//             // this generates a separate chunk (About.[hash].js) for this route
//             // which is lazy-loaded when the route is visited.
//             component: () => import('../views/Layout/MainLayout.vue'),
//             redirect: '/sys/chart/choose',  //总之 我把这里重定向设为第一个界面了，这样每次都进入第一个界面，至于要不要做首页，看你，你首页搞个
//             //  你首页搞个空白的界面也没事，随你。你想要直接就是第一个模块也可以，我个人感觉加一个首页合理一点
//             //  就是一个空白界面，或者放点图？
//             children: [
//                 {
//                     path: 'chart', component: () => import('../views/ChartView/NewChartView.vue'), name: 'newChartView',
//                     redirect: '/sys/chart/choose',
//                     children: [
//                         {
//                             path: 'choose',
//                             component: () => import('../views/ChartView/ChoosePage.vue'),
//                             name: 'chooseView'
//                         },
//                         {
//                             path: 'allchart',
//                             component: () => import('../views/ChartView/AllChartView.vue'),
//                             name: 'allChartView'
//                         },
//                     ]
//                 },
//                 {
//                     path: 'algorithms',
//                     name: 'algorithms',
//                     component: () => import('../views/Algorithms/ModelLayout.vue')
//                 },
//                 {
//                     path: 'pipeline',
//                     component: () => import('../views/Pipeline/PipeView.vue'),
//                     name: 'pipeline'
//                 },
                
//                 {
//                     path: 'datasource',
//                     component: () => import('../views/Layout/DatasourceLayout.vue'),
//                     name: 'datasourceLayout',
//                 },
//                 { path: 'sqllab', component: () => import('../views/SqlLab/SqlLab.vue'), name: 'sqlLab' },
//                 { path: 'mapping', component: () => import('../views/ChartView/ChartMapping.vue'), name: 'chartmapping' },
//                 {
//                     path: 'dashboard',
//                     component: () => import('../views/DashboardView/CreateDashboard.vue'),
//                     name: 'dashboard'
//                 },
//                 {
//                     path: 'dashboardList',
//                     component: () => import('../views/DashboardView/DashboardList.vue'),
//                     name: 'dashboardList'
//                 },
//                 {
//                     path: 'dashboardView',
//                     component: DashboardView,
//                     name: 'dashboardView'
//                 }
//             ]
//         },
//         // {
//         //   path:'/chart/:id',
//         //   name:'detailchart',
//         //   component:() => import('../views/ChartView/DetailChartView.vue')
//         // }
//     ]
// })

// export default router



import { createRouter, createWebHistory } from 'vue-router';
import { DashboardView } from '../views/DashboardView/DashboardView';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            redirect: '/sys'
        },
        {
            path: '/sys',
            name: 'system',
            component: () => import('../views/Layout/MainLayout.vue'),
            redirect: '/sys/chart/choose',
            children: [
                {
                    path: 'chart',
                    component: () => import('../views/ChartView/NewChartView.vue'),
                    name: 'newChartView',
                    redirect: '/sys/chart/choose',
                    children: [
                        {
                            path: 'choose',
                            component: () => import('../views/ChartView/ChoosePage.vue'),
                            name: 'chooseView'
                        },
                        {
                            path: 'allchart',
                            component: () => import('../views/ChartView/AllChartView.vue'),
                            name: 'allChartView'
                        },
                    ]
                },
                {
                    path: 'algorithms',
                    name: 'algorithms',
                    component: () => import('../views/Algorithms/ModelLayout.vue')
                },
                {
                    path: 'pipeline',
                    component: () => import('../views/Pipeline/PipeView.vue'),
                    name: 'pipeline'
                },
                {
                    path: 'datasource',
                    component: () => import('../views/Layout/DatasourceLayout.vue'),
                    name: 'datasourceLayout',
                },
                { path: 'sqllab', component: () => import('../views/SqlLab/SqlLab.vue'), name: 'sqlLab' },
                { path: 'mapping', component: () => import('../views/ChartView/ChartMapping.vue'), name: 'chartmapping' },
                {
                    path: 'dashboard',
                    component: () => import('../views/DashboardView/CreateDashboard.vue'),
                    name: 'dashboard'
                },
                {
                    path: 'dashboardList',
                    component: () => import('../views/DashboardView/DashboardList.vue'),
                    name: 'dashboardList'
                },
                {
                    path: 'dashboardView',
                    component: DashboardView,
                    name: 'dashboardView'
                }
            ]
        },
        {
            path: '/login',
            name: 'login',
            component: () => import('../views/Layout/LoginLayout.vue')
        },
        {
            path: '/register',
            name: 'register',
            component: () => import('../views/Layout/RegisterLayout.vue')
        }
    ]
});
  

export default router;

