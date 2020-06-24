from typing import List
import numpy as np
import cv2

from . import BaseFilter
from ..help import ArgInfo


class Origin(BaseFilter):
    def apply(self, img: np.ndarray):
        return img

    def description(self):
        return "元画像"

    def generate_code(self):
        return ""

    @staticmethod
    def overview() -> str:
        return ""

    @staticmethod
    def method_name() -> str:
        return ""

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("k", "int", "協調パラメータ")
        ]
