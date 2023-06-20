from __future__ import annotations

from src.lib.coins.btc import Btc
from src.lib.coins.eth import Eth
from src.lib.coins.strategy import Strategy
from src.lib.core.exceptions import CoinNotSupportedException


class Coin:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    @classmethod
    def from_string(cls, coin: str) -> Coin:
        match coin:
            case "btc":
                _coin = cls(Btc())
            case "eth":
                _coin = cls(Eth())
            case _:
                raise CoinNotSupportedException("Coin not suppoerted... yet")
        return _coin

    def create_address(self) -> None:
        return self.strategy.create_address()
