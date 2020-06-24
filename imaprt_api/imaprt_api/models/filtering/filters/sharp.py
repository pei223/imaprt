from typing import Dict, List

import numpy as np
import cv2

from . import BaseFilter
from ..help import ArgInfo


class Sharp(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("k") is not None, "鮮鋭化フィルタはkが必要"
        if not isinstance(setting["k"], int):
            raise RuntimeError("鮮鋭化パラメータは整数である必要があります")
        self._k = setting["k"]
        if self._k > 100 or self._k < 1:
            raise RuntimeError("鮮鋭化パラメータは1～99である必要がある")

        self._kernel = np.array([
            [-self._k / 9, -self._k / 9, -self._k / 9],
            [-self._k / 9, 1 + 8 * self._k / 9, -self._k / 9],
            [-self._k / 9, -self._k / 9, -self._k / 9]
        ], np.float32)

    def apply(self, img: np.ndarray):
        return cv2.filter2D(img, -1, self._kernel).astype("uint8")

    def description(self):
        return "K: {}".format(self._k)

    def generate_code(self):
        return """# 鮮鋭化フィルタ
kernel = np.array(
    [[-{k} / 9, -{k} / 9, -{k} / 9], [-{k} / 9, 1 + 8 * {k} / 9, -{k} / 9],
     [-{k} / 9, -{k} / 9, -{k} / 9]], np.float32)
img = cv2.filter2D(img, -1, kernel).astype("uint8")""".format(k=self._k)

    @staticmethod
    def overview() -> str:
        return "ノイズ混入するがエッジ強調"

    @staticmethod
    def method_name() -> str:
        return "sharp"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("k", "int", "協調パラメータ")
        ]
