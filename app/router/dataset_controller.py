from fastapi import APIRouter,Depends
from pydantic import BaseModel

from typing import Union,Dict
from curd.service.dataset_service import SessionLocal,save_dataset,Session,get_all_dataset

router = APIRouter(prefix="/dataset", tags=["dataset"])
# class DataSetConfig:
#     def __init__(self,datasource_id:int,database:str,table:str,
#                  query:str,example_row: Union [Dict , None]):
#         self.datasource_id = datasource_id
#         self.database = database
#         self.table = table
#         self.query = query
#         self.example_row = example_row

class DataSetConfig(BaseModel):
    query:str
    example_row: Union [Dict , None]
    config: Union[Dict,None]
    dataset_name:str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/save")
def save(dataset:DataSetConfig):
    return save_dataset(dataset)

@router.get("/get_all")
def get_all():
    return get_all_dataset()