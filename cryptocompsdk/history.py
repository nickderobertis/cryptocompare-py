from typing import Optional, Any, List, TypeVar, Callable, Type, cast
import pandas as pd

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class ConversionType:
    type: Optional[str]
    conversion_symbol: Optional[str]

    def __init__(self, type: Optional[str], conversion_symbol: Optional[str]) -> None:
        self.type = type
        self.conversion_symbol = conversion_symbol

    @staticmethod
    def from_dict(obj: Any) -> 'ConversionType':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        conversion_symbol = from_union([from_str, from_none], obj.get("conversionSymbol"))
        return ConversionType(type, conversion_symbol)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["conversionSymbol"] = from_union([from_str, from_none], self.conversion_symbol)
        return result


class HistoryRecord:
    time: Optional[int]
    close: Optional[float]
    high: Optional[float]
    low: Optional[float]
    open: Optional[float]
    volumefrom: Optional[float]
    volumeto: Optional[float]

    def __init__(self, time: Optional[int], close: Optional[float], high: Optional[float], low: Optional[float],
                 open: Optional[float], volumefrom: Optional[float], volumeto: Optional[float]) -> None:
        self.time = time
        self.close = close
        self.high = high
        self.low = low
        self.open = open
        self.volumefrom = volumefrom
        self.volumeto = volumeto

    @staticmethod
    def from_dict(obj: Any) -> 'HistoryRecord':
        assert isinstance(obj, dict)
        time = from_union([from_int, from_none], obj.get("time"))
        close = from_union([from_float, from_none], obj.get("close"))
        high = from_union([from_float, from_none], obj.get("high"))
        low = from_union([from_float, from_none], obj.get("low"))
        open = from_union([from_float, from_none], obj.get("open"))
        volumefrom = from_union([from_float, from_none], obj.get("volumefrom"))
        volumeto = from_union([from_float, from_none], obj.get("volumeto"))
        return HistoryRecord(time, close, high, low, open, volumefrom, volumeto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = from_union([from_int, from_none], self.time)
        result["close"] = from_union([to_float, from_none], self.close)
        result["high"] = from_union([to_float, from_none], self.high)
        result["low"] = from_union([to_float, from_none], self.low)
        result["open"] = from_union([to_float, from_none], self.open)
        result["volumefrom"] = from_union([to_float, from_none], self.volumefrom)
        result["volumeto"] = from_union([to_float, from_none], self.volumeto)
        return result


class RateLimit:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'RateLimit':
        assert isinstance(obj, dict)
        return RateLimit()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class HistoricalData:
    response: Optional[str]
    message: Optional[str]
    param_with_error: Optional[str]
    type: Optional[int]
    aggregated: Optional[bool]
    data: Optional[List[HistoryRecord]]
    time_to: Optional[int]
    time_from: Optional[int]
    first_value_in_array: Optional[bool]
    conversion_type: Optional[ConversionType]
    rate_limit: Optional[RateLimit]
    has_warning: Optional[bool]

    def __init__(self, response: Optional[str], message: Optional[str], param_with_error: Optional[str],
                 type: Optional[int], aggregated: Optional[bool], data: Optional[List[HistoryRecord]],
                 time_to: Optional[int], time_from: Optional[int], first_value_in_array: Optional[bool],
                 conversion_type: Optional[ConversionType], rate_limit: Optional[RateLimit],
                 has_warning: Optional[bool]) -> None:
        self.response = response
        self.message = message
        self.param_with_error = param_with_error
        self.type = type
        self.aggregated = aggregated
        self.data = data
        self.time_to = time_to
        self.time_from = time_from
        self.first_value_in_array = first_value_in_array
        self.conversion_type = conversion_type
        self.rate_limit = rate_limit
        self.has_warning = has_warning

    @staticmethod
    def from_dict(obj: Any) -> 'HistoricalData':
        assert isinstance(obj, dict)
        response = from_union([from_str, from_none], obj.get("Response"))
        message = from_union([from_str, from_none], obj.get("Message"))
        param_with_error = from_union([from_str, from_none], obj.get("ParamWithError"))
        type = from_union([from_int, from_none], obj.get("Type"))
        aggregated = from_union([from_bool, from_none], obj.get("Aggregated"))
        data = from_union([lambda x: from_list(HistoryRecord.from_dict, x), from_none, HistoryRecord.from_dict],
                          obj.get("Data"))
        time_to = from_union([from_int, from_none], obj.get("TimeTo"))
        time_from = from_union([from_int, from_none], obj.get("TimeFrom"))
        first_value_in_array = from_union([from_bool, from_none], obj.get("FirstValueInArray"))
        conversion_type = from_union([ConversionType.from_dict, from_none], obj.get("ConversionType"))
        rate_limit = from_union([RateLimit.from_dict, from_none], obj.get("RateLimit"))
        has_warning = from_union([from_bool, from_none], obj.get("HasWarning"))
        return HistoricalData(response, message, param_with_error, type, aggregated, data, time_to, time_from,
                              first_value_in_array, conversion_type, rate_limit, has_warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Response"] = from_union([from_str, from_none], self.response)
        result["Message"] = from_union([from_str, from_none], self.message)
        result["ParamWithError"] = from_union([from_str, from_none], self.param_with_error)
        result["Type"] = from_union([from_int, from_none], self.type)
        result["Aggregated"] = from_union([from_bool, from_none], self.aggregated)
        result["Data"] = from_union([lambda x: from_list(lambda x: to_class(HistoryRecord, x), x), from_none],
                                    self.data)
        result["TimeTo"] = from_union([from_int, from_none], self.time_to)
        result["TimeFrom"] = from_union([from_int, from_none], self.time_from)
        result["FirstValueInArray"] = from_union([from_bool, from_none], self.first_value_in_array)
        result["ConversionType"] = from_union([lambda x: to_class(ConversionType, x), from_none], self.conversion_type)
        result["RateLimit"] = from_union([lambda x: to_class(RateLimit, x), from_none], self.rate_limit)
        result["HasWarning"] = from_union([from_bool, from_none], self.has_warning)
        return result

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.to_dict()['Data'])


def historical_data_from_dict(s: Any) -> HistoricalData:
    return HistoricalData.from_dict(s)


def historical_data_to_dict(x: HistoricalData) -> Any:
    return to_class(HistoricalData, x)
