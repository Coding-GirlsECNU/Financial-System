<!-- <template>
    <div class="w-full h-full">
  
      <div class="w-full h-full" :id="props.chart">
      </div>
  
    </div>
  </template>
  
  
  <script setup>
  import * as echarts from 'echarts';
  import { ref, onMounted, nextTick } from 'vue'
  
  let history = ref([])
  let pred = ref([])
  let returns = ref([])
  let date = ref([])
  let normal_data = ref([])
  let outlier_data = ref([])
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
      type: Object
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
  })
  //7.5 多选功能
  let transferMapping = () => {
    console.log("formData",props.formData)
    let mapping = props.mapping
    // if (!mapping.hasOwnProperty('x_orient') || !mapping.hasOwnProperty('date')) {
    //   console.log('mapping object is not correct', mapping)
    //   return
    // }
    var out = []
    // for (let j = 0; j < mapping.x_orient.length; j++) {
    //   let data = []
    //   for (let i = 0; i < props.formData.length; i++) {
    //     data.push({
    //       returns: props.formData[i][mapping['x_orient'][j]],
    //       date: props.formData[i][mapping['date'][j]]
    //       // name: mapping['returns'][j]
    //     })
    //   }
    let data = []
    for (let i = 0; i < props.formData.length; i++) {
      for (let j = 0; j < props.formData[i].length; j++)
      {
        data.push({
          history: props.formData[i].data.real[j],
          pred: props.formData[i].data.pred[j],
          date: props.formData[i].data.date[j],
        })
      }
      out.push({
        modelName: props.formData[i].modelName,
        Data:data
      })
      // data.push({
      //   returns: props.formData[i][mapping['x_orient'][j]],
      //   date: props.formData[i][mapping['date'][j]]
        // name: mapping['returns'][j]
      // })
      out.push(data)
    }
    console.log("outputData_out",out)
    return out
  }
  
  let getdataTS = () => {
    // let data = transferMapping()
    // console.log("outputData_data",data)
    // data[0].forEach(element => {
    //   history.value.push(element.history);
    //   pred.value.push(element.pred);
    //   date.value.push(element.date);
    // });
    //console.log(returns)
    const dates = [];
  const realValues = [];
  const seriesData = {};

  props.formData.forEach(model => {
    const modelName = model.modelName;
    seriesData[modelName] = [];

    model.data.forEach(item => {
      if (!dates.includes(item.date)) {
        dates.push(item.date);
      }

      if (!realValues.includes(item.real)) {
        realValues.push(item.real);
      }

      seriesData[modelName].push(item.pred);
    });
  });

  return { dates, realValues, seriesData };
  };
  let initTimeSeries = () => { // 初始化时序数据预测图
  
    let chartInstance = echarts.init(document.getElementById(props.chart), 'infographic')
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
        data: ['收益值'],
        top: '4%',
        fontSize: 40
      },
      series: [
  
        {
          name: '收益值',
          type: 'line',
          symbol: 'circle',
          symbolSize: 5,
          data: returns.value,
          color: '#336699'
        },
        
      ],
      tooltip: {
        trigger: 'axis',// 提示框触发方式为轴触发
        axisPointer: {
          type: 'cross', // 坐标轴指示器类型为十字准星
          label: {
            //backgroundColor: 'rgba(0,122,255,0.6)'
            backgroundColor: 'rgba(0,0,0,0.7)', // 提示框标签背景颜色
            fontSize: 14, // 提示框标签字体大小
            padding: [6, 10], // 提示框标签内边距
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
          //rotate: 45, // X 轴标签旋转角度
          fontSize: 12, // X 轴标签字体大小
          color: '#333' // X 轴标签字体颜色
        }
      },
      yAxis: {
        type: 'value',
        axisLabel: {
          fontSize: 13, // Y 轴标签字体大小
          color: '#333' // Y 轴标签字体颜色
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
          console.log(data)
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
    }, 0)
  
  }
  const resizeWindow = () => {
    let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart))
    chartInstance.resize()
  }
  let refreshData = () => {
    returns = ref([])
    date = ref([])
    getdataTS()
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
        data: ['收益值'],
        top: '3%',
        fontSize: 40
      },
      series: [
  
        
        {
          name: '收益值',
          type: 'line',
          symbol: 'circle',
          symbolSize: 5,
          data: returns.value,
          color: '#336699'
        },
        
        
      ],
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
    let chartInstance = echarts.getInstanceByDom(document.getElementById(props.chart))
    chartInstance.setOption(initOption)
  }
  defineExpose({
    refreshData,
    resizeWindow
  })
  onMounted(() => {
    getdataTS()
  
    initTimeSeries()
  })
  
  
  </script>
  
  <style lang="scss" scoped></style> -->

  <template>
    <div class="w-full h-full">
      <div class="w-full h-full" :id="chartId"></div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import * as echarts from 'echarts';
  
  const props = defineProps({
    formData: {
      type: Array,
      required: true
    },
    width: {
      type: Number,
      default: 800
    },
    height: {
      type: Number,
      default: 600
    },
    chartId: {
      type: String,
      default: 'chart'
    }
  });
  
  const chartInstance = ref(null);
  
  // 处理数据
  const processData = () => {
    const dates = new Set();
    const realValues = [];
    const seriesData = {};
  
    props.formData.forEach(model => {
      const modelName = model.modelName;
      seriesData[modelName] = [];
  
      model.data.forEach(item => {
        dates.add(item.date);
        seriesData[modelName].push(item.pred);
      });
  
      // 只处理一次 realValues
      if (realValues.length === 0) {
        model.data.forEach(item => {
          realValues.push(item.real);
        });
      }
    });
  
    return { dates: Array.from(dates), realValues, seriesData };
  };
  
  // 绘制图表
  const renderChart = () => {
    const { dates, realValues, seriesData } = processData();
  
    const series = [
      {
        name: 'Real Value',
        type: 'line',
        data: realValues,
        smooth: true,
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: {
          color: '#5470C6'
        }
      }
    ];
  
    const colors = ['#91CC75', '#FAC858', '#EE6666']; // 你可以自定义更多颜色
    let colorIndex = 0;
  
    for (const [modelName, data] of Object.entries(seriesData)) {
      series.push({
        name: modelName,
        type: 'line',
        data,
        smooth: true,
        symbol: 'circle',
        symbolSize: 8,
        itemStyle: {
          color: colors[colorIndex++ % colors.length]
        }
      });
    }
  
    const option = {
      title: {
        text: 'Real vs Predicted Values',
        left: 'center'
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'cross',
          label: {
            backgroundColor: 'rgba(0,122,255,0.6)'
          }
        },
        formatter: function (params) {
        let tooltipContent = `${params[0].name}<br/>`;
        params.forEach(param => {
          tooltipContent += `${param.marker} ${param.seriesName}: ${param.value}<br/>`;
        });
        return tooltipContent;
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
      // grid: {
      //   left: '3%',
      //   right: '4%',
      //   bottom: '3%',
      //   top: '10%',
      //   containLabel: true,
      // },
      legend: {
        data: ['Real Value', ...Object.keys(seriesData)],
        top: 'bottom'
      },
      xAxis: {
        type: 'category',
        data: dates
      },
      yAxis: {
        type: 'value'
      },
      series,
      // dataZoom: [
      //   {
      //     id: 'dataZoomX',
      //     type: 'slider',
      //     xAxisIndex: [0],
      //     filterMode: 'filter'
      //   }
      // ]
    };
  
    if (chartInstance.value) {
      chartInstance.value.setOption(option);
    }
  };
  
  onMounted(() => {
    chartInstance.value = echarts.init(document.getElementById(props.chartId));
    renderChart();
    window.addEventListener('resize', () => {
    if (chartInstance.value) {
        chartInstance.value.resize();
      }
    });
  });
  
  watch(() => props.formData, renderChart, { deep: true });
  
  </script>
  
  <style scoped>
  .chart-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  