"""
Leader board data model  for leader board and users
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    address = Column(String)
    age= Column(Integer)

    leader_boards = relationship("LeaderBoards", back_populates="user")


class LeaderBoards(Base):
    __tablename__ = "leader_boards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    points = Column(Integer, default=0, nullable=False)

    user = relationship("User", back_populates="leader_boards")