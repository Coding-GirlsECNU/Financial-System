import { api } from '../api'

export function getModels() {
    return api.get('/models/getall')
}