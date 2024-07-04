from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from ..model import Models

from ..sqlconfig import SQLALCHEMY_DATABASE_URL

# SQLALCHEMY_DATABASE_URL = "postgresql://zzh:zzh0117.@113.31.110.212/al"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_all_model():
    db = SessionLocal()
    res = db.query(Models).all()
    db.close()
    return res 