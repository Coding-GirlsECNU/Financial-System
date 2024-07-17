from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

from ..schemas import DataSourceConfig
from sqlalchemy.sql import text
from ..model import DataSource

from ..sqlconfig import SQLALCHEMY_DATABASE_URL

# SQLALCHEMY_DATABASE_URL = "postgresql://zzh:zzh0117.@113.31.110.212/al"
PSQL = "postgresql://{user}:{password}@{host}:{port}/{database}"
SQLALCHEMY_DATABASE_URL_MYSQL = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
MYSQL = "mysql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def show_meta(datasrc:DataSourceConfig):
    # if datasrc.type != "mysql":
    #     raise NotImplementedError()
    try:
        if datasrc.type == "mysql":
            SQL = SQLALCHEMY_DATABASE_URL_MYSQL.format(user=datasrc.user,host=datasrc.host,port=datasrc.port,database=datasrc.database,password=datasrc.password)
            print(SQL)
        else:
            SQL = PSQL.format(user=datasrc.user,host=datasrc.host,port=datasrc.port,database=datasrc.database,password=datasrc.password)
        engine = create_engine(SQL)
        insp = inspect(engine)
        tables = list(insp.get_table_names())
        o = []
        for t in tables:
            tmp = list()
            for j in insp.get_columns(t):
                tmp.append(j['name'])
            o.append({'table':t,'detail':tmp})
        return o
    except Exception as e :
        return {"code":500,"msg":str(e)}

def exec_sql(datasrc:DataSourceConfig):
    try:
        if datasrc.type == "mysql":
            SQL = SQLALCHEMY_DATABASE_URL_MYSQL.format(user=datasrc.user, host=datasrc.host, port=datasrc.port,
                                                       database=datasrc.database, password=datasrc.password)
        else:
            SQL = PSQL.format(user=datasrc.user, host=datasrc.host, port=datasrc.port, database=datasrc.database,
                              password=datasrc.password)
        engine = create_engine(SQL)
        sql = datasrc.query
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            res = result.fetchall()
            if len(res) == 0:
                return []
            columns = res[0]._fields
            out = []
            for item in res:
                item = dict(zip(tuple(columns),tuple(item)))
                out.append(item)
            return out
    except Exception as e :
        print(e)

# login
        
def exec_insert(datasrc: DataSourceConfig):
    try:
        if datasrc.type == "mysql":
            SQL = SQLALCHEMY_DATABASE_URL_MYSQL.format(user=datasrc.user, host=datasrc.host, port=datasrc.port,
                                                       database=datasrc.database, password=datasrc.password)
        else:
            SQL = PSQL.format(user=datasrc.user, host=datasrc.host, port=datasrc.port, database=datasrc.database,
                              password=datasrc.password)
        
        engine = create_engine(SQL)
        Session = sessionmaker(bind=engine)
        session = Session()

        with session.begin():
            result = session.execute(text(datasrc.query))
        
        return {"success": True, "message": "Insert operation successful."}

    except SQLAlchemyError as e:
        error_message = str(e)
        print(error_message)
        return {"success": False, "message": f"Insert operation failed. Error: {error_message}"}



def save_database(payload):
    msg = {'code':200,'msg':'success','data':None}
    try:
        session = SessionLocal()
        database = DataSource(**payload.__dict__)
        db = session
        db.add(database)
        db.commit()
        db.close()
        return msg
    except Exception as e :
        msg['code']=500
        msg['msg'] = 'fail '+ str(e)
        return msg


def delete_datasrc(datasrc_id:int):
    msg = {'code':200,'msg':'success','data':None}
    try:
        session = SessionLocal()
        db = session
        db.query(DataSource).filter(DataSource.datasourceid == datasrc_id).delete()
        db.commit()
        db.close()
        return msg
    except Exception as e :
        msg['code']=500
        msg['msg'] = 'fail '+ str(e)
        return msg





