import pytest

from src.lib.coins.eth import Eth


@pytest.fixture(autouse=True)
def mock_environment_variables(mocker):
    mocker.patch.dict(
        "os.environ",
        {"ZEPLY_PRIVATE_KEY": "df55e88301145178c6226027713bca34fe1b904141335bbba4562d7702e49586"},
    )
    yield


class TestEth:
    def test_create_address(self):
        response = Eth().create_address()
        assert response == "0xC91aF70fBF6f12dAFFEED2c7F523B8895241E14e"
