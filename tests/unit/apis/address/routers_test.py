# pylint: disable=redefined-outer-name
import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

os.environ["PRIVATE_KEY"] = "df55e88301145178c6226027713bca34fe1b904141335bbba4562d7702e49586"

from src.app import app as fast_api_app
from src.lib.core.dependancies import get_db
from src.lib.core.exceptions import CoinNotSupportedException
from src.settings.database import Base
from tests.unit.apis.address import engine


@pytest.fixture(scope="module")
def client(app=fast_api_app):
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def _get_test_db():
        try:
            session = TestingSessionLocal()
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


class TestAddressGetAll:
    def test_get_all_empty(self, client):
        response = client.get("/address/")
        assert response.status_code == 200
        assert [] == response.json()

    def test_get_all(self, mocker, client):
        mocked_coin = mocker.patch("src.apis.address.routers.Coin")
        mocked_coin_from_string = mocker.patch(
            "src.apis.address.routers.Coin.from_string", return_value=mocked_coin
        )
        mocked_coin_create_address = mocker.patch(
            "src.apis.address.routers.Coin.create_address", return_value="test_address"
        )

        payload = {"crypto": "eth"}
        response = client.post("/address/generate", json=payload)
        assert response.status_code == 201

        response = client.get("/address/")
        assert response.status_code == 200
        assert [{"id": 1, "crypto": "eth", "address": "test_address"}] == response.json()

        mocked_coin_from_string.assert_called_once()
        mocked_coin_create_address.assert_called_once()


class TestAddressGetById:
    def test_get_by_id_404(self, client):
        response = client.get("/address/1")
        assert response.status_code == 404
        assert response.json() == {"detail": "Address not found"}

    def test_get_by_id_422(self, client):
        response = client.get("/address/test")
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "loc": ["path", "address_id"],
                    "msg": "value is not a valid integer",
                    "type": "type_error.integer",
                }
            ]
        }

    def test_get_by_id(self, mocker, client):
        mocked_coin = mocker.patch("src.apis.address.routers.Coin")
        mocked_coin_from_string = mocker.patch(
            "src.apis.address.routers.Coin.from_string", return_value=mocked_coin
        )
        mocked_coin_create_address = mocker.patch(
            "src.apis.address.routers.Coin.create_address", return_value="test_address"
        )

        payload = {"crypto": "eth"}
        response = client.post("/address/generate", json=payload)
        assert response.status_code == 201

        response = client.get("/address/1")
        assert response.status_code == 200
        assert {"id": 1, "crypto": "eth", "address": "test_address"} == response.json()

        mocked_coin_from_string.assert_called_once()
        mocked_coin_create_address.assert_called_once()


class TestAddressGenerate:
    def test_generate_400(self, mocker, client):
        mocked_coin_from_string = mocker.patch(
            "src.apis.address.routers.Coin.from_string", side_effect=CoinNotSupportedException
        )

        payload = {"crypto": "eth"}
        response = client.post("/address/generate", json=payload)
        assert response.status_code == 400
        mocked_coin_from_string.assert_called_once()

    def test_generate_422(self, client):
        payload = {"crypto": "test_crypto"}
        response = client.post("/address/generate", json=payload)
        assert response.status_code == 422

    def test_generate(self, mocker, client):
        mocked_coin = mocker.patch("src.apis.address.routers.Coin")
        mocked_coin_from_string = mocker.patch(
            "src.apis.address.routers.Coin.from_string", return_value=mocked_coin
        )
        mocked_coin_create_address = mocker.patch(
            "src.apis.address.routers.Coin.create_address", return_value="test_address"
        )

        payload = {"crypto": "eth"}
        response = client.post("/address/generate", json=payload)
        assert response.status_code == 201

        response = client.get("/address/1")
        assert response.status_code == 200
        assert {"id": 1, "crypto": "eth", "address": "test_address"} == response.json()

        mocked_coin_from_string.assert_called_once()
        mocked_coin_create_address.assert_called_once()
