from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)


engine = create_engine('sqlite:///products.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
