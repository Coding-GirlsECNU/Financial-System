from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
from .. import schemas,model
from ..sqlconfig import SQLALCHEMY_DATABASE_URL
# SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{password}.@{data_url}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
    
def get_all_model_dataset():
    db = SessionLocal()
    db_dataset = db.query(model.ModelDatasets).all()
    db.close()
    return db_dataset

def get_model_dataset(model_name: str, dataset: str, db: Session):
    db=SessionLocal()
    db_model_dataset=db.query(model.ModelDatasets).filter(
        model.ModelDatasets.model_name == model_name,
        model.ModelDatasets.dataset == dataset).all()
    db.close()
    return db_model_dataset
    