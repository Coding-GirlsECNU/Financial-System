from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from curd.sqlconfig import SessionLocal
from curd import schemas, model
from curd.service.dashboard_service import get_all_dashboard, save_dashboard, delete_dashboard

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/getall")
async def get_all(db: Session = Depends(get_db)):
    msg = {"code": 200, "data": None, "msg": "success"}
    res = get_all_dashboard(db)
    if res is not None:
        msg["data"] = res
    else:
        msg["code"] = 500
        msg["msg"] = "fail"
    return msg


@router.post("/save_dashboard")
async def save(payload: schemas.Dashboard, db: Session = Depends(get_db)):
    msg = {"code": 200, "data": None, "msg": "success"}
    dashboard = save_dashboard(db, payload)
    if dashboard is None:
        msg["code"] = 500
        msg["msg"] = "fail"
    else:
        msg["data"] = dashboard
    return msg


@router.delete("/delete_dashboard")
async def delete(payload:schemas.Dashboard, db: Session = Depends(get_db)):
    msg = {"code": 200, "data": None, "msg": "success"}
    res = delete_dashboard(db, payload)
    if res is False:
        msg["code"] = 500
        msg["msg"] = "fail"
        return msg
    res = get_all_dashboard(db)
    msg["data"] = res
    return msg
