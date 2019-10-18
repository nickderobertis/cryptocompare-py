from typing import Optional

from cryptocompsdk.exchanges.parse import Exchanges, CouldNotGetExchangesException, exchanges_from_dict
from cryptocompsdk.request import APIBase
from cryptocompsdk.urls import ALL_EXCHANGE_URL


class ExchangeAPI(APIBase):
    _exception_class = CouldNotGetExchangesException

    def get(self, from_symbol: Optional[str] = None, exchange: Optional[str] = None, top_tier_only: bool = False
            ) -> Exchanges:

        payload = dict(
            fsym=from_symbol,
            e=exchange,
            topTier=top_tier_only
        )

        return super().get(ALL_EXCHANGE_URL, payload)

    def _class_factory(self, data: dict) -> Exchanges:
        return exchanges_from_dict(data)
