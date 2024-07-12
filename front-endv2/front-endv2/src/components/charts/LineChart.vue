<template>
  <div :id="props.cid" class="h-full w-full">
  </div>
  </template>
  
  <script setup>
  import * as echarts from 'echarts'
  import { onMounted, watch } from "vue";
  
  const props = defineProps({
      title: {
      type: String,
      default: ''
      },
      cid: {
      type: String,
      default: ''
      },
      data: {
      type: Object,
      default: () => {
          return {
          x: [],
          y: []
          }
      }
      },
  })
  
  
  onMounted(()=>
  {
      var myChart = echarts.init(document.getElementById(props.cid));
  
      watch(()=>props.data, (newVal, oldVal)=>
      {
      myChart.setOption({
          xAxis: {
              data: newVal.x
          },
          yAxis: {},
          series: [{
              name: 'loss',
              type: 'line',
              data: newVal.y
          }]
          })
      })
      myChart.setOption(
      {
          title: {
          text: props.title,
          textStyle: {
          color: '#333', // 标题文字颜色
          fontSize: 16, // 标题文字大小
          fontWeight: 'bold' // 标题文字粗细
        }
          },
          xAxis: {
          type: "category",
          data: props.data['x'],
          axisLine: { // x轴线样式
          lineStyle: {
            color: '#999' // x轴线颜色
          }
        },
        axisLabel: { // x轴刻度文字样式
          color: '#666', // 刻度文字颜色
          fontSize: 12 // 刻度文字大小
        }
          },
          yAxis: {
          type: "value",
          axisLine: { // y轴线样式
          lineStyle: {
            color: '#999' // y轴线颜色
          }
        },
        axisLabel: { // y轴刻度文字样式
          color: '#666', // 刻度文字颜色
          fontSize: 12 // 刻度文字大小
        }
          },
          series: [{
          data: props.data['y'],
          type: "line",
          symbolSize: 8, // 数据点大小
        lineStyle: { // 折线样式
          width: 2, // 折线宽度
          color: '#1890ff' // 折线颜色
        }
          }]
      }
      );
  })
  
  
  </script>
  
  <style scoped>
  /* 添加组件的样式，可以根据需要进行调整 */
  
  </style>
  