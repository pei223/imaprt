from typing import Dict, List

import numpy as np
import cv2

from . import BaseFilter, GrayScale
from ..help import ArgInfo


class Opening(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None, "Openingはkernel_sizeが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size > 100 or self._kernel_size < 1:
            raise RuntimeError("カーネルサイズは1～99である必要がある")
        self.require_gray_scale = False

    def apply(self, img: np.ndarray):
        if img.ndim == 3:
            self.require_gray_scale = True
            img = GrayScale().apply(img)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((self._kernel_size, self._kernel_size), np.uint8))

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        if self.require_gray_scale:
            return """{gray_scale_code}

# Opening
img = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones(({kernel_size}, {kernel_size}), np.uint8))
""".format(gray_scale_code=GrayScale().generate_code(), kernel_size=self._kernel_size)

        return "# Opening\nimg = cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones(({kernel_size}, {kernel_size}), np.uint8))".format(
            gray_scale_code=GrayScale().generate_code(), kernel_size=self._kernel_size)

    @staticmethod
    def overview() -> str:
        return "画像縮小後に拡大してサイズをもとに戻すことでノイズを除去する"

    @staticmethod
    def method_name() -> str:
        return "opening"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("kernel_size", "int", "拡大・縮小のカーネルサイズ"),
        ]
