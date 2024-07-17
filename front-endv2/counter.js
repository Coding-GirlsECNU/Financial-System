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




import { createStore } from 'vuex';

const store = createStore({
  state: {
    isLoggedIn: false, // 用户登录状态
    username: '', // 用户名
  },
  mutations: {
    // 更新用户登录状态和用户名的 mutation
    setLoggedIn(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    },
    setUsername(state, username) {
      state.username = username;
    },
  },
  actions: {
    // 异步操作，例如登录
    async login({ username }) {
      // 这里可以添加登录逻辑，例如调用API进行验证等
      // 假设验证成功，将用户信息存储到 state 中
      commit('setLoggedIn', true);
      commit('setUsername', username);
    },
    // 退出登录操作
    logout({ commit }) {
      // 清空用户信息
      commit('setLoggedIn', false);
      commit('setUsername', '');
    }
  }
});

export default store;
