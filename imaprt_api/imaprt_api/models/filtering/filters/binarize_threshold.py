from typing import Dict, List

import numpy as np
import cv2
from ..validation_util import *
from . import BaseFilter, GrayScale
from ..help import ArgInfo


class BinarizeThreshold(BaseFilter):
    def __init__(self, setting: Dict[str, int]):
        dict_key_validation(setting, ["lower_threshold", "upper_threshold"], "閾値による2値化")
        int_validation(setting["lower_threshold"], 0, 255, "閾値下限")
        int_validation(setting["upper_threshold"], 0, 255, "閾値上限")
        self._lower_threshold = setting["lower_threshold"]
        self._upper_threshold = setting["upper_threshold"]
        self._require_gray_scale = False

    def apply(self, img: np.ndarray):
        if img.ndim == 3:
            img = GrayScale().apply(img)
            self._require_gray_scale = True

        threshold, img = cv2.threshold(img, self._lower_threshold, self._upper_threshold, cv2.THRESH_BINARY)
        return img

    def description(self):
        return f"閾値: {self._lower_threshold}～{self._upper_threshold}"

    def generate_code(self):
        if self._require_gray_scale:
            return f"{GrayScale().generate_code()}\n\n# 閾値の2値化\nthreshold, img = cv2.threshold(img, {self._lower_threshold}, {self._upper_threshold}, cv2.THRESH_BINARY)"
        return "# 閾値の2値化\nthreshold, img = cv2.threshold(img, {self._lower_threshold}, {self._upper_threshold}, cv2.THRESH_BINARY)"

    @staticmethod
    def overview() -> str:
        return "閾値を設定して二値化"

    @staticmethod
    def method_name() -> str:
        return "binarize_threshold"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("lower_threshold", "int", "閾値下限"),
            ArgInfo("upper_threshold", "int", "閾値上限"),
        ]
