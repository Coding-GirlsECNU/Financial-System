<template>
  <div class="w-full h-full">
    <div class="w-full h-full" :id="props.chart" ref="proChart">

    </div>
  </div>
</template>


<script setup>
import * as echarts from 'echarts';
import { ref, onMounted, nextTick } from "vue";

const props = defineProps({
  width: {
    type: Number,
    default: 800
  },
  height: {
    type: Number,
    default: 600
  },
  formData: {
    type: Object
  },
  mapping: {
    type: Object
  },
  chartType: {
    type: String,
    default: ""
  },
  algorithm: {
    type: String,
    default: ""
  },
  datasource: {
    type: String,
    default: ""
  },
  margin: {
    type: Number,
    default: 4
  },
  chart: {
    type: String,
    default: "proChart"
  },
  mode: {
    type: String
  }
})

let transferMapping = () => {
  let mapping = props.mapping
  if (!mapping.hasOwnProperty('x_orient') || !mapping.hasOwnProperty('x_predict')) {
    console.log('mapping object is not correct', mapping)
    return
  }
  var out = []
  for (let j = 0; j < mapping.x_orient.length; j++) {
    let data = []
    for (let i = 0; i < props.formData.length; i++) {
      data.push({
        x_orient: props.formData[i][mapping['x_orient'][j]],
        X_predict: props.formData[i][mapping['x_predict'][j]],
        date: props.formData[i][mapping['date'][j]],
        name: mapping['x_orient'][j]
      })
    }
    out.push(data)
  }
  let data = []
  let num = out.length;
  for (let i = 0; i < num; i++) {
    let obj = {}
    obj['name'] = out[i][0].name
    obj['x_orient'] = []
    obj['x_predict'] = []
    obj['date'] = []
    for (let j = 0; j < out[i].length; j++) {
      obj['date'].push(out[i][j].date)
      if (out[i][j].x_orient !== null)
        obj['x_orient'].push(out[i][j].x_orient)
      if (out[i][j].X_predict !== null)
        obj['x_predict'].push(out[i][j].X_predict)
    }
    data.push(obj)
  }
  return data
}
let colors = ref(['#91cc75', '#5470c6', '#ee6666', '#7a22ef', '#3bbcd9']);
let legend = ref([]);
let series = ref([]);
let dates = ref([])

function getdata() {
  let data = transferMapping()
  data.forEach((e, index) => {
    let item = {
      name: e.name + "原始值",
      data: e.x_orient,
      type: 'line',
      itemStyle: {
        normal: {
          lineStyle: {
            width: 3,
            type: 'solid',
            color: colors.value[index]  //线的颜色
          },
          color: colors.value[index],  //圈圈的颜色
        }
      }
    }
    series.value.push(item);
    legend.value.push(e.name + "原始值")
    dates.value = e.date
    let arr1 = new Array(e.x_orient.length - 1).fill(null).concat(e.x_orient[e.x_orient.length - 1])
    let arr2 = e.x_predict
    let arr3 = arr1.concat(arr2)

    let item2 = {
      name: e.name + "预测值",
      data: arr3,
      type: 'line',
      itemStyle: {
        normal: {
          lineStyle: {
            width: 3,
            type: 'dotted',
            color: colors.value[index]  //线的颜色
          },
          color: colors.value[index],  //圈圈的颜色
        }
      }
    }
    series.value.push(item2);
    legend.value.push(e.name + "预测值")

  });
  nextTick(() => {
    initTimeSeries()
  })
}


function initTimeSeries() { // 初始化时序数据预测图
  let chartInstance = echarts.init(document.getElementById(props.chart), 'infographic')
  const initOption = {
    legend: {
      // data: this.legend,
      top: '5%'
    },
    series: series.value,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: '#FF9900'
        }
      },
      show: props.mode === 'tooltip_disable' ? false : true
    },
    toolbox: {
      left: '80%',
      top: '4%',
      feature: {
        dataZoom: {
          yAxisIndex: 'none'
        },
        restore: {},
        saveAsImage: {}
      }
    },

    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '15%',
      containLabel: true,
    },
    xAxis: {
      type: 'category',
      data: dates.value
    },

    yAxis: {
      type: 'value'
    },
    dataZoom: [
      {
        id: 'dataZoomX',
        type: 'slider',
        xAxisIndex: [0],
        filterMode: 'filter'
      }
    ],
    animationDuration: 0
  }

  // chartInstance.showLoading({
  //   text: 'loading',
  //   color: '#c23531',
  //   textColor: '#000',
  //   maskColor: 'rgba(255, 255, 255, 0.2)',
  //   zlevel: 0,
  // })
  setTimeout(() => {

    // chartInstance.hideLoading()
    chartInstance.setOption(initOption)
    chartInstance.on('finished', function () {
      if (props.mode === 'pic') {
        let data = chartInstance.getDataURL({
          pixelRatio: 2,
          backgroundColor: '#fff'
        })
        let imgItem = document.createElement('img')
        imgItem.src = data
        // console.log(data)
        imgItem.style.width = '100%'
        imgItem.style.height = '100%'
        let container = document.getElementById(props.chart)?.parentNode
        if (container) {
          container.appendChild(imgItem)
          let ins = document.getElementById(props.chart)
          ins.remove()
          chartInstance.dispose();
        }
      }
    })
  }, 1000)
}

const resizeWindow = () => {
  let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart))
  chartInstance.resize()
}
const refreshData = () => {
  const initOption = {
    legend: {
      // data: this.legend,
      top: '5%'
    },
    series: series.value,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: '#FF9900'
        }
      },
      show: props.mode === 'tooltip_disable' ? false : true

    },
    toolbox: {
      left: '80%',
      top: '4%',
      feature: {
        dataZoom: {
          yAxisIndex: 'none'
        },
        restore: {},
        saveAsImage: {}
      }
    },

    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      top: '15%',
      containLabel: true,
    },
    xAxis: {
      type: 'category',
      data: dates.value
    },

    yAxis: {
      type: 'value'
    },
    dataZoom: [
      {
        id: 'dataZoomX',
        type: 'slider',
        xAxisIndex: [0],
        filterMode: 'filter'
      }
    ],
    animationDuration: 2000
  }

  let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart))
  chartInstance.setOption(initOption)
}


defineExpose({
  refreshData,
  resizeWindow
})
onMounted(() => {
  getdata()
})
</script>

<style lang="scss" scoped></style>