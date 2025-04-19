from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, LargeBinary
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()




class Business(Base):
    __tablename__='Business'
    name=Column(String(255),nullable=False)
    

class Incidents(Base):
    __tablename__='incidents'
    id=Column(Integer,primary_key=True)
    Title=Column(String(255),nullable=False)
    Description=Column(String(500),nullable=False)
