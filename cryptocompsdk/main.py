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
