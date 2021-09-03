from sqlalchemy import desc
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
    users = db.query(data_model.User).order_by(desc(
        data_model.User.points)).offset(skip).limit(limit).all()
    return users


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
    db_user = data_model.User(name=user.name, age=user.age, address=user.address)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_point(db: Session, user: dict, update_type: str) -> dict:
    """
    db_user
    :param update_type:
    :param db: db session
    :param user: queried user data
    """

    if update_type == "inc":
        user.points = user.points + 1
    else:
        if not user.points == 0:
            user.points = user.points - 1
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: dict) -> None:
    """
    delete user from database

    :param db: Database session
    :param user: user  which is going to  be deleted
    :return: None
    """
    db.delete(user)
    db.commit()