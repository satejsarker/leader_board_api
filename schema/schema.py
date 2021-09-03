from typing import List, Optional, Dict, Mapping

from pydantic import BaseModel, Extra


class LeaderBoardBase(BaseModel, extra=Extra.forbid):
    id: int
    user_id: int


class LeaderBoardCreate(LeaderBoardBase):
    pass


class LeaderBoard(BaseModel):
    points: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    name: str
    address: Optional[str]
    age: int
    points: int


class User(UserBase):
    id: int
    name: str
    leader_boards: List[LeaderBoard] = {}

    class Config:
        orm_mode = True