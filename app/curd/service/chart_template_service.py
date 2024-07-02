from fastapi import Depends, HTTPException, status

from app.curd.model import ChartTemplate

from app.curd.sqlconfig import SessionLocal, engine


def get_all_chart_template():
    db = SessionLocal()
    return db.query(ChartTemplate).all()