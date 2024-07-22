<template>
  <div class="register-form">
    <h2>注册</h2>
    <form @submit.prevent="userRegister">
      <div class="form-group">
        <label for="user_id">用户名：</label>
        <input type="text" id="user_id" v-model="user_id" required>
      </div>
      <div class="form-group">
        <label for="password">密码：</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <div class="form-group">
        <label for="tel">手机号：</label>
        <input type="text" id="tel" v-model="tel">
      </div>
      <div class="form-group">
        <label for="verifyCode">验证码：</label>
        <input type="text" id="verifyCode" v-model="verifyCode">
        <sidentify :identifyCode="identifyCode" @click="refreshCode"></sidentify>
      </div>
      <button type="submit">注册新账号</button>
    </form>
    <p>{{ message }}</p> <!-- 显示登录结果的消息 -->
  </div>
</template>


<script>
import { execInsert,execQuery } from '@/api/sqllab/utils';

import { useStore } from 'vuex';
import Sidentify from './Sidentify.vue';

export default {
  components: { Sidentify },
  data() {
    return {
      model:{
        user_id: '',
        password: '',
        tel: '',
        loading: false,
        error: '',
        message:'',
        verifyCode:''
      },
      identifyCodes:"1234567890",
      identifyCode:''
    };
  },

  mounted() {
      // 验证码初始化
      this.identifyCode = '';
      this.makeCode();
  
  },

  methods: {
    //验证码----start
    randomNum(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    },
    refreshCode() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },
    makeCode() {
      for (let i = 0; i < 4; i++) {
        this.identifyCode += this.identifyCodes[
          this.randomNum(0, this.identifyCodes.length)
        ];
      }
      console.log("this.identifyCode:", this.identifyCode);
    },
    //验证码----end

    async userRegister() {
      this.loading = true;
      try {
        const no_same_config = {
          database: "al",
          host: "47.95.213.242",
          password:"zzh0117.",
          port:"5433",
          // query:"SELECT COUNT(*) FROM public.\"user\"",
          // query:"SELECT * FROM public.\"user\" WHERE \"user_id\" = 'userId' AND \"password\" = 'passWord'",
          query:"SELECT * FROM public.\"user\" WHERE \"user_id\" = 'userId'",
          type: "psql",
          user: "postgres"
        };
        //console.log("user_config",user_config)
        const newQuery1 = no_same_config.query.replace(/userId/g, this.user_id);
        const newData = {
          database: "al",
          host: "47.95.213.242",
          password:"zzh0117.",
          port:"5433",
          query:newQuery1,
          type: "psql",
          user: "postgres"
        }
        console.log("Data_history",newData);

        let newResponse = await execQuery(newData);
        console.log('success!');
        const info = newResponse.data;
        console.log("user_info",info);

        var reg = /^(?=.*\d)(?=.*[a-zA-Z])(?=.*[~!@#$%^&*.])[\da-zA-Z~!@#$%^&*.]{6,}$/;
        //密码至少6位，必须包含字母、数字、特殊符号

        if (info.length > 0) {
            this.message = '这个用户名已经被其他用户使用，请换一个吧';
            this.user_id = ''
            this.$forceUpdate();
        }
        else if(!(reg.test(this.password)))
        {
          this.message = '请输入符合要求的密码';
          this.password = '';
          this.$forceUpdate();
        }
        else if(this.tel.length != 11) {
          this.message = '请输入正确的手机号码';
          this.tel = '';
          this.$forceUpdate();
        }
        else if(this.verifyCode != this.identifyCode) {
          this.message = '验证码输入错误';
          this.verifyCode = '';
          this.$forceUpdate();
        }
        else{
          const user_config = {
            database: "al",
            host: "47.95.213.242",
            password:"zzh0117.",
            port:"5433",
            query:"INSERT INTO public.\"user\" (\"user_id\", \"password\", \"tel\") VALUES ('userId','passWord','TEL')",
            type: "psql",
            user: "postgres"
          };
          console.log("user_config",user_config);
          const newQuery1_history = user_config.query.replace(/userId/g, this.user_id);
          const newQuery2_history =newQuery1_history.replace(/passWord/g, this.password);
          const newQuery3_history =newQuery2_history.replace(/TEL/g, this.tel);

          const newData_history = {
            database: "al",
            host: "47.95.213.242",
            password:"zzh0117.",
            port:"5433",
            query:newQuery3_history,
            type: "psql",
            user: "postgres"
          }
          console.log("newData_history",newData_history);

          await execInsert(newData_history);

          console.log('success!');

          this.message = '注册成功!';
          const userId = this.user_id;
          // await store.dispatch('login', { username: this.user_id });
          this.$store.commit('setLoggedIn', true);
          this.$store.commit('setUsername', userId);

          this.$router.push({ name: 'home' });
        }
        
      } catch (error) {
        // 处理错误情况，例如网络错误等
        console.error('注册失败', error);
        this.error = '注册失败，请稍后重试';
      } finally {
        this.loading = false;
      }
    }
  }
}

</script>


<style scoped>
.register-form {
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

button:hover {
  background-color: #45a049;
}
</style>
