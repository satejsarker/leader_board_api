from typing import List

from pydantic import BaseModel


class LeaderBoardBase(BaseModel):
    name: str
    user_id: int


class LeaderBoardCreate(LeaderBoardBase):
    pass


class LeaderBoard(LeaderBoardBase):
    id: int
    user_id: int
    name: str
    scours: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    name: str


class User(UserBase):
    id: int
    name: str
    leader_boards: List[LeaderBoard] = []

    class Config:
        orm_mode = True