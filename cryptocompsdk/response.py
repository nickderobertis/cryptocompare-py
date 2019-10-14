from typing import Optional


class ResponseAPIBase:
    response: Optional[str]

    @property
    def has_error(self) -> bool:
        return self.response == 'Error'
