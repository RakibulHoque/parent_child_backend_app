
# ./app/models.py
import datetime
from sqlalchemy import Column, Boolean, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    full_name = Column(String, unique=True, index=True)
    age = Column(Integer, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, index=True)
    children = relationship(
            "Child",
            back_populates="parent",
            cascade="all, delete, delete-orphan")

class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    full_name = Column(String, index=True)
    age = Column(Integer, index=True)
    parent_id = Column(Integer, ForeignKey("parents.id"))
    parent = relationship("Parent", back_populates="children")

