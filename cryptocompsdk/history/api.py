from typing import Sequence, Optional

from cryptocompsdk.history.parse import HistoricalData, historical_data_from_dict, CouldNotGetHistoryException
from cryptocompsdk.request import _APIBase
from cryptocompsdk.urls import DAILY_HISTORY_URL, HOURLY_HISTORY_URL, MINUTE_HISTORY_URL


class HistoryAPI(_APIBase):

    def get(self, from_symbol: str = 'BTC', to_symbol: Sequence[str] = 'USD', freq: str = 'd',
            exchange: Optional[str] = None, aggregate: Optional[int] = None, end_time: Optional[int] = None,
            limit: int = 100) -> HistoricalData:
        url = self._get_api_url_from_freq(freq)

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
            return DAILY_HISTORY_URL
        elif parsed_freq == 'h':
            return HOURLY_HISTORY_URL
        elif parsed_freq == 'm':
            return MINUTE_HISTORY_URL
        else:
            raise ValueError(f'could not parse frequency {freq}, pass one of d, h, m')