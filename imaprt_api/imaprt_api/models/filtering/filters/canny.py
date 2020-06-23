from typing import Dict

import numpy as np
import cv2

from . import BaseFilter
from ..validation_util import *


class Canny(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        dict_key_validation(setting, ["lower_threshold", "upper_threshold"], "Canny")

        int_validation(setting["lower_threshold"], 0, 255, "閾値下限")
        self._lower_threshold = setting["lower_threshold"]

        int_validation(setting["upper_threshold"], 0, 255, "閾値上限")
        self._upper_threshold = setting["upper_threshold"]

        if self._lower_threshold > self._upper_threshold:
            raise RuntimeError("閾値上限は閾値下限より大きい必要がある")

    def apply(self, img: np.ndarray):
        return cv2.Canny(img, self._lower_threshold, self._upper_threshold).astype("uint8")

    def description(self):
        return f"閾値上限: {self._upper_threshold},  閾値下限: {self._lower_threshold}"

    def generate_code(self):
        return f"# Canny\nimg = cv2.Canny(img, {self._lower_threshold}, {self._upper_threshold}).astype(\"uint8\")"
