from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
import sys
from curd.sqlconfig import SessionLocal
from curd.service import curd
from curd import schemas,model


router = APIRouter(prefix="/datasource", tags=["datasource"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/getall",response_model=List[schemas.DataSource])
async def get_all(db:Session = Depends(get_db)):
    return curd.get_all_datasource(db)

