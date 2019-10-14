from typing import Any, Callable, List, Type, cast, TypeVar, Dict, Union

T = TypeVar("T")


class InvalidTypeException(Exception):
    pass


class NotNoneException(InvalidTypeException):
    pass


class NotIntException(InvalidTypeException):
    pass


class NotFloatException(InvalidTypeException):
    pass


class NotStrException(InvalidTypeException):
    pass


class NotBoolException(InvalidTypeException):
    pass


class NotListException(InvalidTypeException):
    pass


def from_int(x: Any) -> int:
    if isinstance(x, int) and not isinstance(x, bool):
        return x
    raise NotIntException(x)


def from_none(x: Any) -> Any:
    if x is not None:
        raise NotNoneException(x)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except InvalidTypeException:
            pass
    assert False


def from_float(x: Any) -> float:
    if isinstance(x, (float, int)) and not isinstance(x, bool):
        return float(x)
    raise NotFloatException(x)


def from_str(x: Any) -> str:
    if isinstance(x, str):
        return x
    raise NotStrException(x)


def to_float(x: Any) -> float:
    if isinstance(x, float):
        return x
    raise NotFloatException(x)


def from_bool(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    raise NotBoolException(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    if isinstance(x, list):
        return [f(y) for y in x]
    raise NotListException(x)


def from_int_or_str(x: Any) -> Union[str, int]:
    try:
        return int(from_str(x))
    except ValueError:
        return from_str(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }
