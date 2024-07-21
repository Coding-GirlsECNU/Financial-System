<template>
  <div class="w-full h-full">
    <div class="w-full h-full" :id="props.chart"></div>
  </div>
</template>

<script setup>
import * as echarts from 'echarts';
import { ref, onMounted, nextTick } from 'vue';

let returns = ref([]);
let date = ref([]);
const props = defineProps({
  chartType: {
    type: String,
    default: ""
  },
  algorithm: {
    type: String,
    default: ""
  },
  width: {
    type: Number,
    default: 800
  },
  height: {
    type: Number,
    default: 600
  },
  formData: {
    type: Array,
    default: () => []
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
  },
  mapping: {
    type: Object,
    default: {},
    required: true
  }
});

let getdataTS = () => {
  // 初始化 returns 和 date
  let modelNames = Object.keys(props.formData[0]).filter(key => key !== 'date');
  let seriesData = modelNames.map(name => ({
    name,
    data: props.formData.map(item => ({ date: item.date, returns: item[name] }))
  }));

  date.value = props.formData.map(item => item.date);
  returns.value = seriesData;
  console.log(returns.value);
};

let initTimeSeries = () => {
  let chartInstance = echarts.init(document.getElementById(props.chart), 'infographic');
  
  const series = returns.value.map((dataset) => {
    return {
      name: dataset.name,
      type: 'line',
      symbol: 'circle',
      symbolSize: 5,
      data: dataset.data.map(item => item.returns),
      // 为了更好的区分不同的模型，可以给每个模型设置不同的颜色
      color: `#${Math.floor(Math.random()*16777215).toString(16)}` 
    }
  });

  const initOption = {
    title: {
      textAlign: 'center',
      top: 0,
      left: '12%',
      text: props.algorithm,
      subtext: props.datasource,
      textStyle: {
        fontWeight: 'normal',
        fontSize: 50,
        color: 'blue',
        fontFamily: 'Arial',
      },
      subtextStyle: {
        fontSize: 50
      }
    },
    legend: {
      data: series.map(serie => serie.name),
      top: '4%',
      fontSize: 40
    },
    series: series,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: 'rgba(0,0,0,0.7)',
          fontSize: 14,
          padding: [6, 10],
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
      top: '10%',
      containLabel: true,
    },
    xAxis: {
      data: date.value,
      axisLabel: {
        fontSize: 12,
        color: '#333'
      }
    },
    yAxis: {
      type: 'value',
      axisLabel: {
        fontSize: 13,
        color: '#333'
      }
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

  setTimeout(() => {
    chartInstance.setOption(initOption);
    chartInstance.on('finished', function () {
      if (props.mode === 'pic') {
        let data = chartInstance.getDataURL({
          pixelRatio: 2,
          backgroundColor: '#fff'
        });
        let imgItem = document.createElement('img');
        imgItem.src = data;
        console.log(data);
        imgItem.style.width = '100%';
        imgItem.style.height = '100%';
        let container = document.getElementById(props.chart)?.parentNode;
        if (container) {
          container.appendChild(imgItem);
          let ins = document.getElementById(props.chart);
          ins.remove();
          chartInstance.dispose();
        }
      }
    });
  }, 0);
}

const resizeWindow = () => {
  let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart));
  chartInstance.resize();
}

let refreshData = () => {
  returns = ref([]);
  date = ref([]);
  getdataTS();
  const series = returns.value.map((dataset) => {
    return {
      name: dataset.name,
      type: 'line',
      symbol: 'circle',
      symbolSize: 5,
      data: dataset.data.map(item => item.returns),
      color: `#${Math.floor(Math.random()*16777215).toString(16)}`
    }
  });

  const initOption = {
    title: {
      textAlign: 'center',
      top: 0,
      left: '12%',
      text: props.algorithm,
      subtext: props.datasource,
      textStyle: {
        fontWeight: 'normal',
        fontSize: 25,
        color: 'black',
        fontFamily: 'Arial',
      },
      subtextStyle: {
        fontSize: 18
      }
    },
    legend: {
      data: series.map(serie => serie.name),
      top: '3%',
      fontSize: 40
    },
    series: series,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: 'rgba(0,122,255,0.6)'
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
      data: date.value
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

  let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart));
  chartInstance.setOption(initOption);
}

defineExpose({
  refreshData,
  resizeWindow
})

onMounted(() => {
  getdataTS();
  initTimeSeries();
});
</script>

<style lang="scss" scoped></style>
