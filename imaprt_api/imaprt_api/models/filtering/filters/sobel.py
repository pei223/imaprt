from typing import Dict

import numpy as np
import cv2

from . import BaseFilter


class Sobel(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None, "Sobelフィルタはkernel_sizeが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size % 2 == 0 or self._kernel_size > 100 or self._kernel_size < 1:
            raise RuntimeError("カーネルサイズは1～99の奇数である必要がある")

    def apply(self, img: np.ndarray):
        return ((abs(cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=self._kernel_size)) +
                 abs(cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=self._kernel_size))) / 2).astype('uint8')

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        return "# Sobelフィルタ\nimg = ((abs(cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize={kernel_size})) + abs(cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize={kernel_size}))) // 2).astype('uint8')".format(
            kernel_size=self._kernel_size)
