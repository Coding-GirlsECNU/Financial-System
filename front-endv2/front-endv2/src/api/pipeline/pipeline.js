import axios from 'axios';
export function fetchConfig(name) {
    //TODO: change the url
    return axios.get('http://127.0.0.1:8000' + name);
}