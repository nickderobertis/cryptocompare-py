from dataclasses import dataclass
from typing import List, Any, TypeVar, Callable, Type, cast, Optional, Dict

from cryptocompsdk.general.parse import from_int, from_str, from_bool, from_list, to_class, from_union, from_none, \
    from_dict, from_plain_dict
from cryptocompsdk.response import ResponseException, ResponseAPIBase


@dataclass
class RateLimit:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'RateLimit':
        assert isinstance(obj, dict)
        return RateLimit()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class Exchanges(ResponseAPIBase):
    response: Optional[str] = None
    message: Optional[str] = None
    has_warning: Optional[bool] = None
    param_with_error: Optional[str] = None
    type: Optional[int] = None
    rate_limit: Optional[RateLimit] = None
    data: Optional[dict] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Exchanges':
        assert isinstance(obj, dict)
        response = from_union([from_str, from_none], obj.get("Response"))
        message = from_union([from_str, from_none], obj.get("Message"))
        has_warning = from_union([from_bool, from_none], obj.get("HasWarning"))
        param_with_error = from_union([from_str, from_none], obj.get("ParamWithError"))
        type = from_union([from_int, from_none], obj.get("Type"))
        rate_limit = from_union([RateLimit.from_dict, from_none], obj.get("RateLimit"))
        data = from_union([from_plain_dict, from_none], obj.get("Data"))
        return Exchanges(response, message, has_warning, param_with_error, type, rate_limit, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Response"] = from_union([from_str, from_none], self.response)
        result["Message"] = from_union([from_str, from_none], self.message)
        result["HasWarning"] = from_union([from_bool, from_none], self.has_warning)
        result["ParamWithError"] = from_union([from_str, from_none], self.param_with_error)
        result["Type"] = from_union([from_int, from_none], self.type)
        result["RateLimit"] = from_union([lambda x: to_class(RateLimit, x), from_none], self.rate_limit)
        result["Data"] = from_union([from_plain_dict, from_none], self.data)
        return result


def exchanges_from_dict(s: Any) -> Exchanges:
    return Exchanges.from_dict(s)


def exchanges_to_dict(x: Exchanges) -> Any:
    return to_class(Exchanges, x)


class CouldNotGetExchangesException(ResponseException):
    pass
