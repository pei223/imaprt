from typing import Dict, List

import numpy as np

from . import BaseFilter
from ..help import ArgInfo


class BitReverse(BaseFilter):
    def apply(self, img: np.ndarray):
        return 255 - img

    def description(self):
        return ""

    def generate_code(self):
        return "# ビット反転\nimg = 255 - img"

    @staticmethod
    def overview() -> str:
        return "ビット値を反転する"

    @staticmethod
    def method_name() -> str:
        return "bit_reverse"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return []
