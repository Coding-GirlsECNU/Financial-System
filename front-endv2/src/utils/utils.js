export function ExtractData(data, key1, key2) {
  let x = []
  let y = []
  for (let i = 0; i < data.length; i++) {
    x.push(data[i][key1])
    y.push(data[i][key2])
  }
  return { 'x': x, 'y': y }
}

export function decodeURLParam(search) {
  return JSON.parse('{"' + decodeURI(search).replace(/"/g, '\\"').replace(/&/g, '","').replace(/=/g, '":"') + '"}')
}

export function transferMapping(data, mapping) {
  let newData = [];
  let size = data.length;
  for (let i = 0; i < size; i++) {
    newData.push({});
    for (let [oldKey, newKey] of Object.entries(mapping)) {
      if (data[i].hasOwnProperty(oldKey)) {
        newData[i][newKey] = data[i][oldKey];
      }
    }
  }
  return newData;
}



export function GenNonDuplicateID() {
  return Math.random().toString()
}