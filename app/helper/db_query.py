from sqlalchemy.orm import Session

from model import data_model
from schema import schema


def get_user(db: Session, user_id: int) -> dict:
    """
    get user by ID
    :param db: session for db
    :param user_id: user id
    :return: user data
    :rtype: dict
    """
    return db.query(data_model.User).filter(data_model.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> dict:
    """
    get all the users
    :param db: database session
    :param skip: from where it should skip
    :param limit: limit for the data model
    :return:
    """
    return db.query(data_model.User).offset(skip).limit(limit).all()


def get_user_by_name(db: Session, name: str) -> dict:
    """
    Get user by name
    :param db:
    :param name:
    :return:
    """
    return db.query(data_model.User).filter(data_model.User.name == name).first()


def create_new_users(db: Session, user: schema.UserCreate) -> dict:
    """
    create  new user for leader boards

    :return: user dict
    :rtype: dict
    """
    user = data_model.User(name=user.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user