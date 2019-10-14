from typing import Sequence, Optional, Dict, Any
import requests
from cryptocompsdk.history import HistoricalData, historical_data_from_dict, CouldNotGetHistoryException
from cryptocompsdk.urls import DATA_V2_URL


class Request:

    def __init__(self, url: str, payload: Optional[Dict[str, Any]], response: requests.Response):
        self.url = url
        self.payload = payload
        self.response = response

    @property
    def json(self) -> dict:
        return self.response.json()

class _APIBase:

    def __init__(self, api_key: str):
        self.api_key = api_key

    def request(self, url: str, payload: Optional[Dict[str, Any]] = None) -> Request:
        api_key_dict = {'api_key': self.api_key}
        payload = self.filter_payload(payload)
        if payload is not None:
            payload.update(api_key_dict)
        else:
            payload = api_key_dict

        result = requests.get(url, params=payload)
        return Request(url, payload, result)

    def filter_payload(self, payload: Optional[Dict[str, Any]]):
        if payload is None:
            return payload

        return {key: value for key, value in payload.items() if value is not None}


class HistoryAPI(_APIBase):

    def get(self, from_symbol: str = 'BTC', to_symbol: Sequence[str] = 'USD', freq: str = 'd',
            exchange: Optional[str] = None, aggregate: Optional[int] = None, end_time: Optional[int] = None,
            limit: int = 100) -> HistoricalData:
        url_base = 'histo'
        url_base += self._get_api_url_from_freq(freq)
        url = DATA_V2_URL + url_base

        payload = dict(
            fsym=from_symbol,
            tsym=to_symbol,
            e=exchange,
            aggregate=aggregate,
            limit=limit,
            toTs=end_time,
        )

        data = self.request(url, payload)
        history = historical_data_from_dict(data.json)
        if history.has_error:
            raise CouldNotGetHistoryException(f'Requested {url} with payload {self.filter_payload(payload)}, '
                                              f'got {data} as response')
        history._request = data
        return history

    def _get_api_url_from_freq(self, freq: str) -> str:
        parsed_freq = freq.lower().strip()[0]
        if parsed_freq == 'd':
            return 'day'
        elif parsed_freq == 'h':
            return 'hour'
        elif parsed_freq == 'm':
            return 'minute'
        else:
            raise ValueError(f'could not parse frequency {freq}, pass one of d, h, m')



class CryptoCompare(_APIBase):

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.history = HistoryAPI(api_key)







