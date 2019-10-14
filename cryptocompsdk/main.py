from cryptocompsdk.request import _APIBase
from cryptocompsdk.history.api import HistoryAPI


class CryptoCompare(_APIBase):

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.history = HistoryAPI(api_key)