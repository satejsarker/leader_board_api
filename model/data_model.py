"""
Leader board data model  for leader board and users
"""

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    address = Column(String)
    age = Column(Integer)
    points = Column(Integer, default=0, nullable=False)