from typing import List
import cv2
import numpy as np

from .base_filter import BaseFilter
from ..help.arg_info import ArgInfo


class GrayScale(BaseFilter):
    def apply(self, img: np.ndarray) -> np.ndarray:
        if img.ndim == 2:
            return img
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def description(self):
        return "グレースケール"

    def generate_code(self):
        return "# グレースケール\nimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)"

    @staticmethod
    def overview() -> str:
        return "色のついている画像を白黒にする"

    @staticmethod
    def method_name() -> str:
        return "gray_scale"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return []
