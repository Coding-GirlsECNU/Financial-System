import axios from "axios";
let api = axios.create({
    baseURL: "http://localhost:7900"})

export function getConfig(){
   return axios({
        url:'/al2',
        method: "POST",
        headers:{'Content-Type':'application/json'},
        data:JSON.stringify({
            "method":"TrainError.GetConfig",
            "params":[]
        })
    })
}

export function getError(){
    return axios({
        url:'/al2',
        method: "POST",
        headers:{'Content-Type':'application/json'},
        data:JSON.stringify({
            "method":"TrainError.GetError",
            "params":[{
                "id":"1676013446"
            }]
        })
    })
}