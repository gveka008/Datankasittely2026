from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

#Mallia alembic exercise main

Base = declarative_base()

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