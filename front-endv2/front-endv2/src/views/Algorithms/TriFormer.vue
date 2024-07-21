<template>
    <div class="w-full h-full flex">
        <div class="flex-none ">
            <ConfigList v-if="config" :config="config"></ConfigList>
        </div>
        <div class="flex-1 ">
            <div class="w-full h-full" v-if="data">
                <!--TODO: 这里都需要从后端返回 -->
                <LineChart class="w-full h-1/3" cid="train_loss" :data="ExtractData(data, 'epoch', 'train_loss')"
                    title="train_loss" />
                <LineChart class="w-full h-1/3" cid="valid_loss" :data="ExtractData(data, 'epoch', 'valid_loss')"
                    title="valid_loss" />
                <LineChart class="w-full h-1/3" cid="test_loss" :data="ExtractData(data, 'epoch', 'test_loss')"
                    title="test_loss" />
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getConfig, getError } from '../../api/al2/algorithm2';
import LineChart from '../../components/charts/LineChart.vue';
import ConfigList from '../../components/algorithm/ConfigList.vue';
const router = useRouter();
//TODO:// 这些都是暂时的 都应该从数据库取值然后渲染，包括图的个数类型等等，这些都是后端返回的
let config = ref(null)
let data = ref(null)
let ExtractData = (data, key1, key2) =>{
    let x = []
    let y = []
    for(let i=0;i<data.length;i++)
    {
        x.push(data[i][key1])
        y.push(data[i][key2])
    }
    return {'x':x,'y':y}
    }
getConfig().then((res) => {
    config.value = res.data.result;
})
getError().then((res) => {
    data.value = res.data.result["train_dict"];
})

</script>