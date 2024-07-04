from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from apputils import global_object
print(global_object.config)
SQLALCHEMY_DATABASE_URL = (f"postgresql://{global_object.config['app']['user']}:"
                           f"{global_object.config['app']['password']}"
                           f"@"
                           f"{global_object.config['app']['database_url']}:{global_object.config['app']['port']}"
                           f"/"
                           f"{global_object.config['app']['database']}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

