#  ./app/schemas.py
from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class PersonBase(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int]


class ChildCreate(PersonBase):
    pass


class Child(PersonBase):
    id: int
    parent_id: int

    class Config:
        orm_mode = True


class ParentCreate(PersonBase):
    address: str
    email: str


class Parent(PersonBase):
    id: int
    address: str
    email: str
    children: Optional[List[Child]] = []

    class Config:
        orm_mode = True
