from typing import Dict

import numpy as np
import cv2

from . import BaseFilter
from ..validation_util import *


class Bilateral(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        dict_key_validation(setting, ["sigma_space", "sigma_color", "diameter"], "バイラテラルフィルタ")

        float_validation(setting["sigma_color"], 0.0, 100.0, "色標準偏差")
        self._sigma_color = setting["sigma_color"]

        float_validation(setting["sigma_space"], 0.0, 100.0, "距離標準偏差")
        self._sigma_space = setting["sigma_space"]

        int_validation(setting["diameter"], 0, 100, "領域")
        self._diameter = setting["diameter"]

    def apply(self, img: np.ndarray):
        return cv2.bilateralFilter(img, d=self._diameter, sigmaColor=self._sigma_color, sigmaSpace=self._sigma_space).astype("uint8")

    def description(self):
        return f"領域: {self._diameter},  色標準偏差: {self._sigma_color},  距離標準偏差: {self._sigma_space}"

    def generate_code(self):
        return f"# バイラテラルフィルタ\nimg = cv2.bilateralFilter(img, d={self._diameter}, sigmaColor={self._sigma_color}, sigmaSpace={self._sigma_space}).astype(\"uint8\")"
