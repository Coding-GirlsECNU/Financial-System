import {api,axios} from "@/api/axios";

export function saveDataSrc(payload) {
    return api({
        url:'/datasrc/save_datasrc',
        data:payload,
        method:'post'
    })
}
export function deleteDataSrc(payload) {
    return api({
        url:'/datasrc/delete_datasrc/'+payload.toString(),
        method:'delete'
    })
}