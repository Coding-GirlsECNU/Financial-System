<template>
  <div class="register-form">
    <div class="register-box">
      <div class="header">注 册</div>
 
      <el-form @submit.prevent="userRegister">
        <div class="input-row">
          <div class="form-group">
            <label for="user_id">用户名：</label>
            <input type="text" id="user_id" v-model="user_id" required>
          </div>  
          <div class="note">请输入您的用户名</div>
        </div>
        <div class="input-row">
          <div class="form-group">
            <label for="password">密码：</label>
            <input type="password" id="password" v-model="password" required>
          </div>
          <div class="note">密码应至少为6位，不能包含空格和特殊字符</div>
        </div>
        <div class="input-row">
          <div class="form-group">
            <label for="tel">手机号：</label>
            <input type="text" id="tel" v-model="tel">
          </div>
          <div class="note">请输入正确的手机号码</div>
        </div>
        <div class="input-row">
          <div class="form-group">
            <label for="verifyCode">验证码：</label>
            <input type="text" id="verifyCode" v-model="verifyCode">
            <sidentify :identifyCode="identifyCode" @click="refreshCode"></sidentify>
          </div>
          <div class="notee">看不清？点击换一张</div>
        </div>
        <button type="submit" class="btn">注 册 新 账 号</button>
      </el-form>
      <p>{{ message }}</p> <!-- 显示登录结果的消息 -->
    </div>
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

        if (info.length > 0) {
            this.message = '这个用户名已经被其他用户使用，请换一个吧';
            this.user_id = ''
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
  height: 100%;
  background-image: linear-gradient(to right, #fbc2eb, #a6c1ee);
}

.input-row {
  margin-bottom: 15px; /* 调整行间距 */
}

.form-group {
  display: flex;
  align-items: center;
}

.form-group label {
  flex: 0 0 80px; /* 固定标签宽度 */
  margin-right: 10px; /* 标签和输入框之间的间距 */

}

.register-box {
  background-color: #fff;
  width: 358px;
  height: 588px;
  border-radius: 15px;
  padding: 0 50px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.header {
  font-size: 38px;
  font-weight: bold;
  text-align: center;
  line-height: 200px;
}

.btn {
  text-align: center;
  padding: 10px;
  width: 100%;
  margin-top: 40px;
  background-image: linear-gradient(to right, #a6c1ee, #fbc2eb);
  color: #fff;
  font-weight: bold;
}

.note {
  margin-top: 5px;
  font-size: 12px;
  color: #888;
  margin-left: 100px;
}

.notee {
  margin-top: 5px;
  font-size: 12px;
  color: #888;
  margin-left: 250px;
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
