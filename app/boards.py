"""
Leader boards api
"""
from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

import app.helper.db_query as db_query
from model import data_model
from model.database import SessionLocal, engine
from schema import schema

data_model.Base.metadata.create_all(bind=engine)

USER = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@USER.post('/', status_code=status.HTTP_201_CREATED, response_model=schema.User)
async def user_creation(user: schema.UserCreate,
                        db: Session = Depends(get_db)) -> dict:
    """
    Create new user

    :param user: user data
    :param db: db Session
    :return: newly created user data
    :rtype: JSONResponse
    """
    db_user = db_query.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists with same "
                                                    "name :{}".format(user.name))
    return db_query.create_new_users(db, user)


@USER.get('/', status_code=status.HTTP_200_OK, response_model=List[schema.User])
async def get_all_user(skip: int = 0, limit: int = 100,
                       db: Session = Depends(get_db)) -> dict:
    """
    get all users

    :param db:  database session
    :param limit: how many users
    :param skip: skipped from from
    :return: all the users
    :rtype: JSONResponse
    """
    db_users = db_query.get_users(db, skip=skip, limit=limit)
    if not db_users:
        raise HTTPException(status_code=404, detail="no user found")
    return db_users


@USER.patch("/{user_id}", status_code=status.HTTP_200_OK, response_model=schema.User)
async def update_points(user_id: int, board: schema.LeaderBoardUpdate,
                        db: Session = Depends(get_db)) -> dict:
    """
    update a user point value (add or remove by one )

    :param board: point board
    :param user_id:  user id for the leader board update
    :param db: database session
    :return: None
    """
    db_user = db_query.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")

    return db_query.update_point(db, db_user, board.update_type)


@USER.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Session = Depends(get_db)) -> JSONResponse:
    """
    Delete a user
    :param user_id: user id for deletion
    :param db: Database session
    :return: success json response
    """
    db_user = db_query.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="user not found")
    db_query.delete_user(db, db_user)
    return JSONResponse({
        "msg": f"user with name : `{db_user.name}` deleted successfully"
    })