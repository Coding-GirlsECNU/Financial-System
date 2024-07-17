from fastapi import APIRouter, Depends,HTTPException
import json
from curd.service import datasrc_meta
from curd.service.datasrc_meta import save_database, delete_datasrc
from curd.schemas import DataSource

router = APIRouter(prefix="/datasrc", tags=["datasrc"])
class DataSourceConfig:
    def __init__(self,config:dict):
        print(config)
        self.host = config['host']
        self.port = config['port'] 
        self.user = config['user']
        self.password = config['password']
        self.type = config.get('type','mysql')
        self.database = config['database']
        self.table = config.get('table',None)
        self.query = config.get('query',None)


@router.post("/meta")
def get_meta(datameta:DataSourceConfig = Depends(DataSourceConfig)):
    try:
        meta = datasrc_meta.show_meta(datameta)
        print(meta)
        return meta
    except Exception as e :
        raise HTTPException(status_code=500,detail=str(e)+'get meta failed')

@router.post("/execquery")
def exec_query(datameta:DataSourceConfig = Depends(DataSourceConfig)):
    try:
        meta = datasrc_meta.exec_sql(datameta)
        return meta
    except Exception as e :
        raise HTTPException(status_code=500,detail=str(e)+'something wrong with your sql query')



@router.post("/execinsert")
def execinsert(datameta:DataSourceConfig = Depends(DataSourceConfig)):
    try:
        meta = datasrc_meta.exec_insert(datameta)
        return meta
    except Exception as e :
        raise HTTPException(status_code=500,detail=str(e)+'something wrong with your sql query')


@router.post("/save_datasrc")
async def save_database_controller(database:DataSource):
    msg = save_database(database)
    return msg

@router.delete("/delete_datasrc/{datasrc_id}")
async def delete_datasrc_controller(datasrc_id:int):
    msg = delete_datasrc(datasrc_id)
    return msg