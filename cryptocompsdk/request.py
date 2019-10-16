from typing import Optional, Dict, Any, Callable
import requests

from cryptocompsdk.response import ResponseException


class Request:

    def __init__(self, url: str, payload: Optional[Dict[str, Any]], response: requests.Response):
        self.url = url
        self.payload = payload
        self.response = response

    @property
    def json(self) -> dict:
        return self.response.json()


class APIBase:
    _exception_class = ResponseException

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

    def get(self, url: str, payload: Optional[Dict[str, Any]] = None):
        data = self.request(url, payload)
        obj = self._class_factory(data.json)
        if obj.has_error:
            if payload is not None:
                payload_str = f'payload {payload}'
            else:
                payload_str = 'no payload'
            raise self._exception_class(f'Requested {url} with {payload_str}, '
                                            f'got {data} as response')
        obj._request = data
        return obj

    def _class_factory(self, data: dict):
        raise NotImplementedError('must implement in subclass')






