from typing import Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


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
    type: str
    conversion_symbol: str

    def __init__(self, type: str, conversion_symbol: str) -> None:
        self.type = type
        self.conversion_symbol = conversion_symbol

    @staticmethod
    def from_dict(obj: Any) -> 'ConversionType':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        conversion_symbol = from_str(obj.get("conversionSymbol"))
        return ConversionType(type, conversion_symbol)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["conversionSymbol"] = from_str(self.conversion_symbol)
        return result


class HistoryRecord:
    time: int
    close: float
    high: float
    low: float
    open: float
    volumefrom: float
    volumeto: float

    def __init__(self, time: int, close: float, high: float, low: float, open: float, volumefrom: float,
                 volumeto: float) -> None:
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
        time = from_int(obj.get("time"))
        close = from_float(obj.get("close"))
        high = from_float(obj.get("high"))
        low = from_float(obj.get("low"))
        open = from_float(obj.get("open"))
        volumefrom = from_float(obj.get("volumefrom"))
        volumeto = from_float(obj.get("volumeto"))
        return HistoryRecord(time, close, high, low, open, volumefrom, volumeto)

    def to_dict(self) -> dict:
        result: dict = {}
        result["time"] = from_int(self.time)
        result["close"] = to_float(self.close)
        result["high"] = to_float(self.high)
        result["low"] = to_float(self.low)
        result["open"] = to_float(self.open)
        result["volumefrom"] = to_float(self.volumefrom)
        result["volumeto"] = to_float(self.volumeto)
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
    response: str
    type: int
    aggregated: bool
    data: List[HistoryRecord]
    time_to: int
    time_from: int
    first_value_in_array: bool
    conversion_type: ConversionType
    rate_limit: RateLimit
    has_warning: bool

    def __init__(self, response: str, type: int, aggregated: bool, data: List[HistoryRecord], time_to: int,
                 time_from: int, first_value_in_array: bool, conversion_type: ConversionType, rate_limit: RateLimit,
                 has_warning: bool) -> None:
        self.response = response
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
        response = from_str(obj.get("Response"))
        type = from_int(obj.get("Type"))
        aggregated = from_bool(obj.get("Aggregated"))
        data = from_list(HistoryRecord.from_dict, obj.get("Data"))
        time_to = from_int(obj.get("TimeTo"))
        time_from = from_int(obj.get("TimeFrom"))
        first_value_in_array = from_bool(obj.get("FirstValueInArray"))
        conversion_type = ConversionType.from_dict(obj.get("ConversionType"))
        rate_limit = RateLimit.from_dict(obj.get("RateLimit"))
        has_warning = from_bool(obj.get("HasWarning"))
        return HistoricalData(response, type, aggregated, data, time_to, time_from, first_value_in_array,
                              conversion_type, rate_limit, has_warning)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Response"] = from_str(self.response)
        result["Type"] = from_int(self.type)
        result["Aggregated"] = from_bool(self.aggregated)
        result["Data"] = from_list(lambda x: to_class(HistoryRecord, x), self.data)
        result["TimeTo"] = from_int(self.time_to)
        result["TimeFrom"] = from_int(self.time_from)
        result["FirstValueInArray"] = from_bool(self.first_value_in_array)
        result["ConversionType"] = to_class(ConversionType, self.conversion_type)
        result["RateLimit"] = to_class(RateLimit, self.rate_limit)
        result["HasWarning"] = from_bool(self.has_warning)
        return result


def historical_data_from_dict(s: Any) -> HistoricalData:
    return HistoricalData.from_dict(s)


def historical_data_to_dict(x: HistoricalData) -> Any:
    return to_class(HistoricalData, x)
