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
    users=db.query(data_model.User).offset(skip).limit(limit).all()
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
    leader_board = data_model.LeaderBoards(points=user.points)
    db_user.leader_boards.append(leader_board)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user