<template>
  <div class="login-form">
    <div class="header">
      <h2>登录</h2>
      <button type="text" @click="goToRegister">还没有账号？注册新账号</button>
    </div>
    <form @submit.prevent="userLogin">
      <div class="form-group">
        <label for="user_id">用户名：</label>
        <input type="text" id="user_id" v-model="user_id" required>
      </div>
      <div class="form-group">
        <label for="password">密码：</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">登录</button>
    </form>
    <p>{{ message }}</p> <!-- 显示登录结果的消息 -->
  </div>
</template>


<script>
import { execQuery } from '@/api/sqllab/utils';

import { useStore } from 'vuex';

export default {
  data() {
    return {
      user_id: '',
      password: '',
      loading: false,
      error: '',
      message:''
    };
  },
  methods: {
    async userLogin() {
      this.loading = true;
      try {
        const user_config = {
          database: "al",
          host: "47.95.213.242",
          password:"zzh0117.",
          port:"5433",
          query:"SELECT * FROM public.\"user\" WHERE \"user_id\" = 'userId' AND \"password\" = 'passWord'",
          type: "psql",
          user: "postgres"
        };
        //console.log("user_config",user_config)
        const newQuery1_history = user_config.query.replace(/userId/g, this.user_id);
        const newQuery2_history =newQuery1_history.replace(/passWord/g, this.password);
        const newData_history = {
          database: "al",
          host: "47.95.213.242",
          password:"zzh0117.",
          port:"5433",
          query:newQuery2_history,
          type: "psql",
          user: "postgres"
        }
        //console.log("user_config",newData_history)

        let response = await execQuery(newData_history);
        const user_info = response.data;
        //console.log("user_info",user_info)

        if (user_info.length > 0) {
          // 登录成功，跳转到下一个页面或者执行其他逻辑
          //console.log('登录成功');
          this.message = '登录成功!';
          const userId = this.user_id;
          // await store.dispatch('login', { username: this.user_id });
          this.$store.commit('setLoggedIn', true);
          this.$store.commit('setUsername', userId);

          this.$router.push({ name: 'home' });
        } else {
          // 登录失败，显示错误消息或者清空输入框
          //console.log('用户名或密码错误');
          this.user_id = '';
          this.password = '';
          this.message = '用户名或密码错误';
        }
      } catch (error) {
        // 处理错误情况，例如网络错误等
        console.error('登录失败', error);
        this.error = '登录失败，请稍后重试';
      } finally {
        this.loading = false;
      }
    },
    async goToRegister() {
      this.$router.push({ name: 'register' });
    }

  }
}

</script>


<style scoped>
.login-form {
  max-width: 300px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

</style>
