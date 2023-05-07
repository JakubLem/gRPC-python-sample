from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

DATABASE_URL = "sqlite:///products.db"

engine = create_engine(DATABASE_URL, poolclass=NullPool, connect_args={"check_same_thread": False})


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
