"""
Test request and response schema
"""
from uuid import uuid4

from pydantic import ValidationError
from pytest import fixture, raises

from schema.schema import UserCreate, LeaderBoardUpdate


@fixture(scope="class")
def common_user_data() -> dict:
    """
    Common user data
    :return:  user data in dict format
    """
    return {
        "name": uuid4().hex,
        "age": 36,
        "address": "test_local"
    }


class TestUserCreateSchema:
    """
    Test user create schema
    """

    # @cached_property
    # def user_create_schema(self):
    #     return UserCreate

    def test_user_valid_data(self, common_user_data: dict):
        """
        test user valid data
        :param common_user_data: common user data pytest fixture
        """
        user_create_schema = UserCreate(**common_user_data)
        assert user_create_schema.age
        assert user_create_schema.name
        assert user_create_schema.address

    def test_invalid_user_create_data(self, common_user_data: dict):
        """"
         Test Invalid user data

        :param common_user_data:  common user data pytest fixture
        """
        common_user_data.pop("name")

        with raises(ValidationError):
            UserCreate(**common_user_data)

    def test_leader_valid_board_update(self):
        """
        Test leader board update schema valid data
        :return:
        """
        update_type = LeaderBoardUpdate(update_type="inc")
        assert update_type.update_type
        update_type = LeaderBoardUpdate(update_type="dec")
        assert update_type.update_type

    def test_leader_invalid_board_update(self):
        """
        Test leader board update schema invalid data
        :return:
        """
        with raises(ValidationError):
            LeaderBoardUpdate(update_type="some_value")