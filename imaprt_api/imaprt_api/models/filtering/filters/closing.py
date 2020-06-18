from typing import Dict

import numpy as np
import cv2

from . import BaseFilter, GrayScale


class Closing(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None, "Closingはkernel_sizeが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size > 100 or self._kernel_size < 1:
            raise RuntimeError("カーネルサイズは1～99である必要がある")
        self._require_gray_scale = False

    def apply(self, img: np.ndarray):
        if img.ndim == 3:
            self._require_gray_scale = True
            img = GrayScale().apply(img)
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((self._kernel_size, self._kernel_size), np.uint8))

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        if self._require_gray_scale:
            return """{gray_scale_code}

# Closing
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones(({kernel_size}, {kernel_size}), np.uint8))
""".format(gray_scale_code=GrayScale().generate_code(), kernel_size=self._kernel_size)

        return "# Closing\nimg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones(({kernel_size}, {kernel_size}), np.uint8))".format(
            gray_scale_code=GrayScale().generate_code(), kernel_size=self._kernel_size)
