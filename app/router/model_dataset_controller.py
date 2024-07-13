from fastapi import APIRouter,Depends
from pydantic import BaseModel

from typing import Union,Dict
from curd.service.model_dataset_service import SessionLocal,Session,get_all_model_dataset

router = APIRouter(prefix="/model_dataset", tags=["model_dataset"])
# class DataSetConfig:
#     def __init__(self,datasource_id:int,database:str,table:str,
#                  query:str,example_row: Union [Dict , None]):
#         self.datasource_id = datasource_id
#         self.database = database
#         self.table = table
#         self.query = query
#         self.example_row = example_row


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get_all")
def get_all():
    return get_all_model_dataset()