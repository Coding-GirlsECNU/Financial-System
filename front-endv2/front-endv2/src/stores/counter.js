import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import {useLocalStorage} from '@vueuse/core'
import {api} from "../api/axios"

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})

export const useBootstrapStore = defineStore('bootstrap', () => {
  const bootstrap = useLocalStorage('bootstrap', {});
  let  setBootstrap = async () => {
   return await api.get('/bootstrap').then((res) => {
      bootstrap.value = res.data
      localStorage.setItem('bootstrap', JSON.stringify(bootstrap.value))
    })
  }
  return  {setBootstrap,bootstrap}

})