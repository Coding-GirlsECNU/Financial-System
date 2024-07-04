import { createRouter, createWebHistory } from 'vue-router'
import { DashboardView } from '../views/DashboardView/DashboardView'
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
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import('../views/Layout/MainLayout.vue'),
            redirect: '/sys/algorithms',
            children: [
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
                    path: 'chart', component: () => import('../views/ChartView/NewChartView.vue'), name: 'newChartView',
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
                    path: 'datasource',
                    component: () => import('../views/Layout/DatasourceLayout.vue'),
                    name: 'datasourceLayout',
                },
                { path: 'sqllab', component: () => import('../views/SqlLab/SqlLab.vue'), name: 'sqlLab' },
                { path: 'mapping', component: () => import('../views/ChartView/ChartMapping.vue'), name: 'chartmapping' },
                {
                    path: 'dashboard',
                    component: () => import('../views/DashboardView/CreateDashbord.vue'),
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
        }
        // {
        //   path:'/chart/:id',
        //   name:'detailchart',
        //   component:() => import('../views/ChartView/DetailChartView.vue')
        // }
    ]
})

export default router
