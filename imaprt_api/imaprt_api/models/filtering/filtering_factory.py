from typing import Dict
import json
from rest_framework.exceptions import ParseError

from . import *

KEY_METHOD = "method"


def create(params: Dict) -> BaseFilter:
    if isinstance(params, str):
        params = params.replace("'", '"')
        params = json.loads(params)
    method_name = params[KEY_METHOD]
    if method_name is None:
        raise ParseError(f"フィルター名が必要")

    if method_name == "gaussian":
        return Gaussian(params)
    elif method_name == "median":
        return Median(params)
    elif method_name == "sharp":
        return Sharp(params)
    elif method_name == "sobel":
        return Sobel(params)

    elif method_name == "gray_scale":
        return GrayScale()
    elif method_name == "binarize_otsu":
        return BinarizeOtsu()

    elif method_name == "closing":
        return Closing(params)
    elif method_name == "opening":
        return Opening(params)

    raise RuntimeError(f"無効なメソッド名: {method_name}")
