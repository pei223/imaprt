from typing import Dict, List

import numpy as np
import cv2
from ..validation_util import *
from . import BaseFilter, GrayScale
from ..help import ArgInfo


class BinarizeAdaptive(BaseFilter):
    def __init__(self, setting: Dict[str, int]):
        dict_key_validation(setting, ["kernel_size", "c"], "適応的2値化")
        odd_validation(setting["kernel_size"], 0, 500, "カーネルサイズ")
        int_validation(setting["c"], -500, 500, "定数")
        self._kernel_size = setting["kernel_size"]
        self._c = setting["c"]
        self._require_gray_scale = False

    def apply(self, img: np.ndarray):
        if img.ndim == 3:
            img = GrayScale().apply(img)
            self._require_gray_scale = True

        return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, self._kernel_size,
                                     self._c)

    def description(self):
        return f"カーネルサイズ: {self._kernel_size}　定数: {self._c}"

    def generate_code(self):
        if self._require_gray_scale:
            return f"{GrayScale().generate_code()}\n\n# 適応的2値化\nimg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, {self._kernel_size}, {self._c})"
        return f"# 適応的2値化\nimg = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, {self._kernel_size}, {self._c})"

    @staticmethod
    def overview() -> str:
        return "適応的二値化"

    @staticmethod
    def method_name() -> str:
        return "binarize_adaptive"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("kernel_size", "int", "カーネルサイズ"),
            ArgInfo("c", "int", "計算されたしきい値から引く定数"),
        ]
