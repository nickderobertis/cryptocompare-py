from cryptocompsdk.blockchain.available.parse import CouldNotGetBlockchainAvailableCoinsException
from cryptocompsdk.request import APIBase
from cryptocompsdk.urls import BLOCKCHAIN_AVAILABLE_COINS_URL


class BlockchainAvailableCoinsAPI(APIBase):
    _exception_class = CouldNotGetBlockchainAvailableCoinsException

    def get(self):
        # TODO: add return type
        return self._get_one_or_paginated(BLOCKCHAIN_AVAILABLE_COINS_URL)

    def _class_factory(self, data: dict):
        # TODO: blockchain class factory
        return data
