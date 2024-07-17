<script setup>
import {RouterView } from 'vue-router'
import {ref} from 'vue'
import { useBootstrapStore } from './stores/counter';
const bootstrapStore = useBootstrapStore();
bootstrapStore.setBootstrap().then(()=>{
});

</script>

<template>
  <RouterView />
</template>

<style>
html,body,#app {
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}
</style>
