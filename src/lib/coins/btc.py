from bitcoin import decode_privkey, encode_privkey, privtopub, pubtoaddr

from src.lib.coins.strategy import Strategy
from src.settings.settings import settings


class Btc(Strategy):
    def create_address(self) -> str:
        private_key = encode_privkey(decode_privkey(settings.private_key, "hex"), "wif")
        public_key = privtopub(private_key)
        return pubtoaddr(public_key)
