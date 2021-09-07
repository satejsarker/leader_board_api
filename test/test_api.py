"""
all API endpoint  test
"""
from uuid import uuid4

from _pytest.compat import cached_property
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


class TestApi:
    """
    API testing Class
    """

    @cached_property
    def new_user_payload(self) -> dict:
        """
        create a payload for new user creation

        :return: new user payload
        :rtype: dict
        """
        return {
            "name": uuid4().hex,
            "age": 36,
            "address": "test_local"
        }

    def test_get_all_users(self) -> None:
        """
        Test get request for all the users requests

        :return:
        """
        res = client.get('/users')
        assert res.status_code == 200
        assert type(res.json()) == list

    def test_invalid_request(self) -> None:
        """
        Test invalid request which will return 404
        :return:
        """

        res = client.get("/random_url")
        assert res.status_code == 404
        assert res.json() == {'detail': 'Not Found'}

    def test_create_new_user(self) -> None:
        """
        Test create new user
        :return:
        """
        res = client.post("/users/", headers={"X-Token": "coneofsilence"},
                          json=self.new_user_payload)
        assert res.status_code == 201
        user_id = res.json().get("id")
        assert user_id
        client.delete(f"/users/{user_id}")

    def test_increase_point(self) -> None:
        """
        test increase score
        :return:
        """
        new_user = client.post("/users/", headers={"X-Token": "coneofsilence"},
                               json=self.new_user_payload).json()
        assert new_user.get("points") == 0
        user_id = new_user.get("id")
        point_inc_res = client.patch(f"/users/{user_id}", json={
            "update_type": "inc"
        })
        assert point_inc_res.status_code == 200
        assert point_inc_res.json().get("points") == 1
        client.delete(f"/users/{user_id}")

    def test_dec_point(self) -> None:
        """
        test increase score
        :return:
        """
        new_user = client.post("/users/", headers={"X-Token": "coneofsilence"},
                               json=self.new_user_payload).json()
        assert new_user.get("points") == 0
        user_id = new_user.get("id")
        point_dec_res = client.patch(f"/users/{user_id}", json={
            "update_type": "dec"
        })
        assert point_dec_res.status_code == 200
        assert point_dec_res.json().get("points") == 0

        client.patch(f"/users/{user_id}", json={
            "update_type": "inc"
        })
        client.patch(f"/users/{user_id}", json={
            "update_type": "inc"
        })

        point_dec_res = client.patch(f"/users/{user_id}", json={
            "update_type": "dec"
        })
        assert point_dec_res.status_code == 200
        assert point_dec_res.json().get("points") == 1

        client.delete(f"/users/{user_id}")

    def test_delete_user(self) -> None:
        """
        Test Delete user API
        :return:
        """
        user_data = self.new_user_payload
        new_user = client.post("/users/", headers={"X-Token": "coneofsilence"},
                               json=user_data).json()
        user_id = new_user.get("id")

        delete_res = client.delete(f"/users/{user_id}")
        assert delete_res.status_code == 200
        assert delete_res.json() == {
            "msg": f"user with name : `{user_data['name']}` deleted successfully"
        }