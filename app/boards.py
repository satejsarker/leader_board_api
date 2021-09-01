"""
Leader boards api
"""
from model import data_model
from model.database import SessionLocal, engine
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import app.helper.db_query as db_query
from schema import schema

data_model.Base.metadata.create_all(bind=engine)

LEADER_BOARDS = APIRouter()
USER = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@LEADER_BOARDS.get('/', status_code=status.HTTP_200_OK)
async def all_leaders() -> JSONResponse:
    data = {
        "msg": "this is initial api"
    }
    return JSONResponse(data)


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
    print(user)
    db_user = db_query.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists with same "
                                                    "name :{}".format(user.name))
    return db_query.create_new_users(db, user)