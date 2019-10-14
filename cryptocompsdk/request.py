from typing import Optional, Dict, Any
import requests


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







