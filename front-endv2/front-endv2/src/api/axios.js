import axios from "axios";
let api = axios.create({
    baseURL: "http://localhost:8000/",
});
export  {api,axios}