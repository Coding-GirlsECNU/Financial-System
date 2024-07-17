
import {axios,api} from "@/api/axios";

export function saveBoard(payload) {
    return api({
        url: '/dashboard/save_dashboard',
        data:payload,
        method:'post'
    })
}

export function deleteBoard(payload){
    return api({
        url:'/dashboard/delete_dashboard',
        data:payload,
        method:'delete'
    })
}