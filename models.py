from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime, LargeBinary
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Business(Base):
    __tablename__ = 'businesses'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    employees = relationship("Employee", back_populates="business", cascade="all, delete-orphan")
    incidents = relationship("Incident", back_populates="business", cascade="all, delete-orphan")


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)

    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    business = relationship("Business", back_populates="employees")

    reported_incidents = relationship("Incident", back_populates="reporter")


class Incident(Base):
    __tablename__ = 'incidents'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=False)
    severity = Column(String(50), nullable=False)  # e.g., Low, Medium, High, Critical
    status = Column(String(50), default="Open")  # e.g., Open, In Progress, Resolved, Closed
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    business_id = Column(Integer, ForeignKey('businesses.id'), nullable=False)
    reporter_id = Column(Integer, ForeignKey('employees.id'), nullable=False)

    business = relationship("Business", back_populates="incidents")
    reporter = relationship("Employee", back_populates="reported_incidents")
