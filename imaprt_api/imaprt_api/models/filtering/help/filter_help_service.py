from typing import Dict, List

from ..filters import *

filter_class_list = [Bilateral, BinarizeOtsu, Canny, Closing, Gaussian, GrayScale, Laplacian, Median, Opening, Sharp,
                     Sobel]


def generate_help_json() -> List[Dict]:
    result = []
    for filter_class in filter_class_list:
        args_result = []
        for arg_info in filter_class.args_info():
            args_result.append(arg_info.to_dict())
        result.append({
            "filterName": filter_class.method_name(),
            "overview": filter_class.overview(),
            "argList": args_result
        })
    return result
