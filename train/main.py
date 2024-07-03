import json
import uuid

import uvicorn
import random
from fastapi import FastAPI, Request
from typing import Dict, List
from pydantic import BaseModel
from curd.db_setting import Datasrc
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import threading
from threading import Thread
import multiprocessing
import os 
import time
import asyncio
import re 
import subprocess

# class triformer(Trainer):
#     def __init__(self, model, config):
#         super().__init__(model, config)

#     def start_train(self):
#         print("start train")

#     def get_predict(self):
#         print("get predict")

#     def write_to_db(self, config):
#         pass


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class train_request(BaseModel):
    model_name: str
    config: Dict | None
    dataset: Dict | None
    mapping: List | None


"""
cnf参数如下
{"model_name":"triformer", 
“predict”：false,
"dataset": {"datasetid":10,"query":"select * from ETTh1 limit 
10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n","config":{"host":"113.31.110.212","port":"3306","user":"root","password":"zzh0117.",
"type":"mysql","database":"db11","query":"select * from ETTh1 limit 10;\n\n\n\n\n\n\n\n\n\n\n\n\n\n"},
"example_row":{
"date":"2016-07-01 00:00:00","HUFL":"5.827000141143799","HULL":"2.009000062942505","MUFL":"1.5989999771118164",
"MULL":"0.4620000123977661","LUFL":"4.203000068664552","LULL":"1.3400000333786009","OT":"30.5310001373291"},
"dataset_name":"ETTH1"},
"mapping":[{"value":"date","label":"x","type":"select","desc":"横坐标,用于表示时序","axis":"date"},{"value":"X","label":"y_true","type":"select","desc":"纵坐标,用于表示实际值","axis":"HUFL"}],
"config":{}}
"""
def exec_parse_write(db:Datasrc, cmd, table_name):
    print("training start")
    db.create_table([('x', 'int'), ('y', 'float'),('z','float')])

    file_check_event = threading.Event()

    file_thread = threading.Thread(target=spy_file, args=(db,table_name, file_check_event))
    file_thread.start()

    process = subprocess.Popen(f"{cmd} > {table_name}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    process.wait()

    file_check_event.set()

    file_thread.join()

def spy_file(db:Datasrc,table_name, file_check_event):
    while not file_check_event.is_set():
        if os.path.exists(table_name):
            with open(table_name, 'r') as file:
                data = file.read()
                x_values = [int(match.group(1)) for match in re.finditer(r'x:(\d+)', data)]
                y_values = [ random.random() for i in range(len(x_values))]
                z_values = [ random.random() for i in range(len(x_values))]
            db.clear_table()
            for i in range(len(x_values)):
                db.insert_into(['x','y','z'],[x_values[i],y_values[i],z_values[i]],['int','float','float'])
        time.sleep(1) 

    print("File monitoring thread is terminating.")




async def run_long_running_function(*args):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, exec_parse_write,*args)


@app.get("/train")
async def train_model(cnf: str):
    request = json.loads(cnf)
    dataset = request['dataset']
    print(dataset, type(dataset))
    data_src = dataset['config']
    msg = {"code": 200, "data": {"host": data_src['host'], "port": data_src['port'],
                                 "user": data_src['user'], "password": data_src['password'],
                                 "database": data_src['database'], "table_name": None,"example_row":{"x":1,"y":0.2,"z":0.3}}}
    try:
        table_name = uuid.uuid4().hex
        database_connection = Datasrc(host=data_src['host'], port=int(data_src['port']),
                                      user=data_src['user'], password=data_src['password'],
                                      database=data_src['database'],
                                      table_name=table_name)
        # 从mapping里拿出用于训练的列名
        x = request['mapping'][0]['axis'] # x=['date', 'HUFL', 'HULL', 'MUFL', 'MULL', 'LUFL', 'LULL'],y=['OT']
        y = request['mapping'][1]['axis']

        # 构造训练数据从数据库里拿，保存读出到的数据到本地，然后调用训练脚本
        query = dataset['query'] # 省略读取数据的代码

        # 调用训练脚本
        asyncio.create_task(run_long_running_function(database_connection,"cd /Users/jan/Desktop/aivis && ./test.sh ",table_name))

        msg['data']['table_name'] = table_name
        return msg

    except Exception as e:
        print("err", e)
        msg['code'] = 500
        msg['data'] = None
    return msg


@app.get("/predict")
async def test():
    asyncio.create_task(run_long_running_function(None,"cd /Users/jan/Desktop/aivis && ./test.sh ",'111'))
    
    return {"code": 200, "data": "ok"}

if __name__ == '__main__':
    uvicorn.run(app, port=5678)
