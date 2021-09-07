"""
User data schema for all the endpoints
"""
from enum import Enum

from pydantic import BaseModel, Extra


class LeaderBoardUpdateEnum(str, Enum):
    increment = "inc"
    decrement = "dec"


class LeaderBoardUpdate(BaseModel, extra=Extra.forbid):
    update_type: LeaderBoardUpdateEnum = LeaderBoardUpdateEnum.increment


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase, extra=Extra.forbid):
    name: str
    address: str
    age: int


class User(UserBase):
    id: int
    name: str
    address: str
    age: str
    points: int

    class Config:
        orm_mode = True