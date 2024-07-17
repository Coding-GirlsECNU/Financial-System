import { api } from '../axios'

export function getDatasrcMeta(config) {
    return api.post('/datasrc/meta', config)
}

export function execQuery(config) {
    return api.post('/datasrc/execquery', config)
}

export function execInsert(config) {
    return api.post('/datasrc/execinsert', config)
}

export function saveDataset(config) {
    return api.post('/dataset/save', config)
}