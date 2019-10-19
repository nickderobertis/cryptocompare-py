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

        # Remove None values as they were just defaults
        without_none = {key: value for key, value in payload.items() if value is not None}

        # Convert booleans into boolean strings that API is expecting
        with_str_bools = {key: _bool_to_str_if_bool(value) for key, value in without_none.items()}

        return with_str_bools

    def get(self, url: str, payload: Optional[Dict[str, Any]] = None):
        data = self.request(url, payload)
        obj = self._class_factory(data.json)
        # isinstance dict added for development of api where class has not been set yet
        if isinstance(obj, dict):
            return obj
        if obj.has_error:
            if payload is not None:
                payload_str = f'payload {payload}'
            else:
                payload_str = 'no payload'
            raise self._exception_class(f'Requested {url} with {payload_str}, '
                                            f'got {data.json} as response')
        obj._request = data
        return obj

    def _class_factory(self, data: dict):
        raise NotImplementedError('must implement in subclass')


def _bool_to_str(boolean: bool) -> str:
    if not isinstance(boolean, bool):
        raise ValueError(f'non-boolean {boolean} passed to _bool_to_str')

    if boolean:
        return 'true'

    return 'false'


def _bool_to_str_if_bool(obj: Any) -> Any:
    if not isinstance(obj, bool):
        return obj
    return _bool_to_str(obj)
