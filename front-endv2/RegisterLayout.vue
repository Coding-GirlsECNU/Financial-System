<template>
  <div class="login-form">
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
      <button type="submit">注册新账号</button>
    </form>
    <p>{{ message }}</p> <!-- 显示登录结果的消息 -->
  </div>
</template>


<script>
import { execInsert,execQuery } from '@/api/sqllab/utils';

import { useStore } from 'vuex';

//import Client from 'pg';

//const { Client } = require('pg');

export default {
  data() {
    return {
      user_id: '',
      password: '',
      tel: '',
      loading: false,
      error: '',
      message:''
    };
  },
  methods: {
    async userRegister() {
      this.loading = true;
      try {
        // const query = "INSERT INTO public.\"user\" (\"user_id\", \"password\", \"tel\") VALUES ('userId','passWord','TEL')"
        // const newQuery1_history = query.replace(/userId/g, this.user_id);
        // const newQuery2_history =newQuery1_history.replace(/passWord/g, this.password);
        // const newQuery3_history =newQuery2_history.replace(/TEL/g, this.tel);

        // const client = new Client({
        //     database: "al",
        //     host: "47.95.213.242",
        //     password:"zzh0117.",
        //     port:"5433",
        //     query:newQuery3_history,
        //     type: "psql",
        //     user: "postgres"
        // })
        // const new_query = client.query;

        // client.connect((err) =>{
        //   if (err) throw err;
        //   console.log('connected!');
        // })

        // client.query('BEGIN', (err) => {
        //   if (err) throw err;
        //   client.query(new_query, (err, res) => {
        //     if (err) throw err;
        //   })

        //   client.query('COMMIT', (err) => {
        //     if (err) {
        //       client.query('ROLLBACK', (err) => {
        //         if (err) throw err;
        //       })
        //     }
        //     console.log('success!');
        //   })
        // })

        // app.post('/upload', upload.single('file'), (req, res) => {
        //   const filePath = req.file.path;
        //   const results = [];
        // })

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

        // const config = {
        //   database: "al",
        //   host: "47.95.213.242",
        //   password:"zzh0117.",
        //   port:"5433",
        //   // query:"SELECT COUNT(*) FROM public.\"user\"",
        //   query:"SELECT * FROM public.\"user\" WHERE \"user_id\" = 'userId' AND \"password\" = 'passWord'",
        //   // query:"SELECT * FROM public.\"user\" WHERE \"user_id\" = 'userId'",
        //   type: "psql",
        //   user: "postgres"
        // };
        // //console.log("user_config",user_config)
        // const Query1_history = config.query.replace(/userId/g, this.user_id);
        // const Query2_history =Query1_history.replace(/passWord/g, this.password);
        // const Data_history = {
        //   database: "al",
        //   host: "47.95.213.242",
        //   password:"zzh0117.",
        //   port:"5433",
        //   query:Query2_history,
        //   type: "psql",
        //   user: "postgres"
        // }
        // console.log("Data_history",Data_history);

        // let response = await execQuery(Data_history);
        // console.log('success!');
        // const user_info = response.data;
        // console.log("user_info",user_info);
        
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

button:hover {
  background-color: #45a049;
}
</style>
