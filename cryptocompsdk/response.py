from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from cryptocompsdk.request import Request


class ResponseAPIBase:
    response: Optional[str]
    _request: 'Request'

    @property
    def has_error(self) -> bool:
        return self.response == 'Error'


class ResponseException(Exception):
    pass