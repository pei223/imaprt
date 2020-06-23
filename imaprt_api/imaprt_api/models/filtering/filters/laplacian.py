from typing import Dict

import numpy as np
import cv2

from . import BaseFilter
from ..validation_util import *


class Laplacian(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        dict_key_validation(setting, ["kernel_size"], "ラプラシアンフィルタ")
        odd_validation(setting["kernel_size"], min_val=1, max_val=99, variable_name="カーネルサイズ")
        self._kernel_size = setting["kernel_size"]

    def apply(self, img: np.ndarray):
        return cv2.Laplacian(img, cv2.CV_64F, ksize=self._kernel_size).astype("uint8")

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        return f"# ラプラシアンフィルタ\nimg = cv2.Laplacian(img, cv2.CV_64F, {self._kernel_size}).astype(\"uint8\")"
