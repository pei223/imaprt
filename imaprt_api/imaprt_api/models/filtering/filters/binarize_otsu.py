from typing import Dict

import numpy as np
import cv2

from . import BaseFilter, GrayScale


class BinarizeOtsu(BaseFilter):
    def __init__(self):
        self._threshold = -1
        self._require_gray_scale = False

    def apply(self, img: np.ndarray):
        if img.ndim == 3:
            img = GrayScale().apply(img)
            self._require_gray_scale = True

        threshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self._threshold = threshold
        return img

    def description(self):
        if self._threshold == -1:
            return ""
        return "閾値: {}".format(str(self._threshold))

    def generate_code(self):
        if self._require_gray_scale:
            return "{gray_scale_code}\n\n# 大津の2値化\nthreshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)".format(
                gray_scale_code=GrayScale().generate_code())
        return "# 大津の2値化\nthreshold, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)"
