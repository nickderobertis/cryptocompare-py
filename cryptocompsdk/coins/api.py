from cryptocompsdk.coins.parse import coins_from_dict, CouldNotGetCoinsException
from cryptocompsdk.request import APIBase
from cryptocompsdk.urls import COIN_LIST_URL


class CoinsAPI(APIBase):

    def get(self):
        data = self.request(COIN_LIST_URL)
        coins = coins_from_dict(data.json)
        if coins.has_error:
            raise CouldNotGetCoinsException(f'Requested {COIN_LIST_URL} with no payload, '
                                              f'got {data} as response')
        coins._request = data
        return coins
