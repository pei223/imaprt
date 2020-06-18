from typing import Dict

import numpy as np
import cv2

from . import BaseFilter


class Median(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None, "メディアンフィルタはkernel_sizeが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size > 100 or self._kernel_size < 1:
            raise RuntimeError("カーネルサイズは1～99である必要がある")

    def apply(self, img: np.ndarray):
        return cv2.medianBlur(img, self._kernel_size)

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        return "# メディアンフィルタ\nimg = cv2.medianBlur(img, {})".format(str(self._kernel_size))
