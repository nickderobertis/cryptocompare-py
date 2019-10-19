from typing import Dict

from cryptocompsdk.exchanges.info.api import ExchangeInfoAPI
from cryptocompsdk.exchanges.symbols.api import ExchangeSymbolsAPI
from cryptocompsdk.request import APIBase
from cryptocompsdk.history.api import HistoryAPI
from cryptocompsdk.coins.api import CoinsAPI
from cryptocompsdk.social.api import SocialAPI


class CryptoCompare(APIBase):

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.history = HistoryAPI(api_key)
        self.coins = CoinsAPI(api_key)
        self.social = SocialAPI(api_key)
        self.exchange_symbols = ExchangeSymbolsAPI(api_key)
        self.exchange_info = ExchangeInfoAPI(api_key)

        self._coin_response = None

    @property
    def coin_ids(self) -> Dict[str, int]:
        try:
            return self._coin_response.symbol_id_dict
        except AttributeError:
            self._coin_response = self.coins.get()
            return self._coin_response.symbol_id_dict
