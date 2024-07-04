from .sqlconfig import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON


class DataSource(Base):
    __tablename__ = "datasource"
    datasourceid = Column(Integer, primary_key=True, index=True)
    config = Column(JSON)


class Chart(Base):
    __tablename__ = "chart"
    chartid = Column(Integer, primary_key=True, index=True,autoincrement=True)
    config = Column(JSON)
    dataset = Column(JSON)
    mapping = Column(JSON)


class Dashboard(Base):
    __tablename__ = "dashboard"
    dashboardid = Column(Integer, primary_key=True, index=True)
    charts = Column(JSON)
    layout = Column(JSON)
    dashboard_name = Column(String)


class DataSet(Base):
    __tablename__ = "dataset"
    datasetid = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    example_row = Column(JSON)
    config = Column(JSON)
    dataset_name = Column(String)


class ChartTemplate(Base):
    __tablename__ = "chart_template"
    cid = Column(Integer, primary_key=True, index=True)
    chart_name = Column(String)
    config = Column(JSON)


class Models(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String)
    model_config = Column(JSON)

class ModelDatasets(Base):
    __tablename__='model_dataset'
    model_name=Column(String, primary_key=True)
    dataset=Column(String, primary_key=True)
    model_config=Column(JSON)