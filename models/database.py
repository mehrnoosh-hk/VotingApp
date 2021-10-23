from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


_DB_URI = "sqlite:///./pools"
engine = create_engine()

Base = declarative_base(
    _DB_URI, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(bind=engine)
