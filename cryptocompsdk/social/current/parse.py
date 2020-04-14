from typing import Optional, Any, Dict, Union, List

import pandas as pd

from cryptocompsdk.general.parse import from_int, from_none, from_union, from_float, from_str, to_float, from_bool, \
    from_dict, to_class, is_type, from_int_or_str, from_na, from_str_number
from cryptocompsdk.response import ResponseAPIBase, ResponseException




class CouldNotGetSocialLatestException(ResponseException):
    pass
