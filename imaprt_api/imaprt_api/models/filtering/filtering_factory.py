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

    if method_name == Gaussian.method_name():
        return Gaussian(params)
    elif method_name == Median.method_name():
        return Median(params)
    elif method_name == Sharp.method_name():
        return Sharp(params)

    elif method_name == Sobel.method_name():
        return Sobel(params)
    elif method_name == Laplacian.method_name():
        return Laplacian(params)
    elif method_name == Canny.method_name():
        return Canny(params)

    elif method_name == GrayScale.method_name():
        return GrayScale()
    elif method_name == BinarizeOtsu.method_name():
        return BinarizeOtsu()

    elif method_name == Closing.method_name():
        return Closing(params)
    elif method_name == Opening.method_name():
        return Opening(params)

    elif method_name == Bilateral.method_name():
        return Bilateral(params)

    raise RuntimeError(f"無効なメソッド名: {method_name}")
