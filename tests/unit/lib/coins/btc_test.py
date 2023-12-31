import pytest


@pytest.fixture(autouse=True)
def mock_environment_variables(mocker):
    mocker.patch.dict(
        "os.environ",
        {"PRIVATE_KEY": "df55e88301145178c6226027713bca34fe1b904141335bbba4562d7702e49586"},
    )
    yield


class TestBtc:
    def test_create_address(self):
        from src.lib.coins.btc import Btc
        response = Btc().create_address()
        assert response == "132HwTr4AQQAnzZ41zgqVjoE4hDMLN58FZ"
