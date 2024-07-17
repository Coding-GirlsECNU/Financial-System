<template>
    <div class="w-full h-full bg-zinc-50 m-0 p-0">
        <Board class="w-full h-full" v-if="charts.length > 0" :chart="charts"></Board>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { getAllChart } from "@/api/chart/chartApi";
import { Board } from './SpiltPane'
import 'splitpanes/dist/splitpanes.css'

let charts = ref([])

getAllChart().then(res => {
    charts.value = res.data.data
    charts.value.map(item => {
        item.key = item.chartid
    })
})



</script>

<style></style>