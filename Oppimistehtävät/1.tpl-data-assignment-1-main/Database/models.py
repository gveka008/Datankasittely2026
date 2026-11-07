from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#Mallia alembic exercise main

#Define base class for models
Base = declarative_base()

#Define user model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    city = Column(String)
    phone = Column(String)
    website = Column(String)
    company_name = Column(String)