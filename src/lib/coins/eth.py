from eth_keys import keys

from src.lib.coins.strategy import Strategy
from src.settings.settings import settings


class Eth(Strategy):
    def create_address(self) -> str:
        private_key_bytes = bytes.fromhex(settings.private_key)
        eth_key = keys.PrivateKey(private_key_bytes)
        address = eth_key.public_key.to_checksum_address()
        return address
