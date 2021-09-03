"""
all API endpoint  test
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestApi:
    """
    API testing Class
    """

    def test_get_all_users(self) -> None:
        """
        Test get request for all the users requests

        :return:
        """
        res = client.get('/users')
        assert res.status_code == 200
        assert type(res.json()) == list