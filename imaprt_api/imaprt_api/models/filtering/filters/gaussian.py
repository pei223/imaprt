from typing import Dict, List

import numpy as np
import cv2

from . import BaseFilter
from ..help import ArgInfo


class Gaussian(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None and setting.get(
            "sigma") is not None, "ガウシアンフィルタはkernel_size, sigmaが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size % 2 == 0 or self._kernel_size > 100 or self._kernel_size < 1:
            raise RuntimeError("カーネルサイズは1～99の奇数である必要がある")

        if not isinstance(setting["sigma"], float) and not isinstance(setting["sigma"], int):
            raise RuntimeError("sigmaは小数か整数である必要がある")
        self._sigma = setting["sigma"]
        if not 0.0 <= self._sigma <= 100.0:
            raise RuntimeError("Sigmaは0,0～100.0である必要がある")

    def apply(self, img: np.ndarray):
        return cv2.GaussianBlur(img, (self._kernel_size, self._kernel_size), self._sigma)

    def description(self):
        return "カーネルサイズ: {},  分散: {}".format(self._kernel_size, self._sigma)

    def generate_code(self):
        return "# ガウシアンフィルタ\nimg = cv2.GaussianBlur(img, ({}, {}), {})".format(str(self._kernel_size),
                                                                               str(self._kernel_size),
                                                                               str(self._sigma))

    @staticmethod
    def overview() -> str:
        return "ノイズ除去"

    @staticmethod
    def method_name() -> str:
        return "gaussian"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("sigma", "float or int", "標準偏差"),
            ArgInfo("kernel_size", "odd int", "カーネルサイズ"),
        ]
