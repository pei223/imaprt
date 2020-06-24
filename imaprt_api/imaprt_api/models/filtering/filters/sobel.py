from typing import Dict, List

import numpy as np
import cv2

from . import BaseFilter
from ..help import ArgInfo


class Sobel(BaseFilter):
    def __init__(self, setting: Dict[str, any]):
        assert setting.get("kernel_size") is not None, "Sobelフィルタはkernel_sizeが必要"
        if not isinstance(setting["kernel_size"], int):
            raise RuntimeError("カーネルサイズは整数である必要があります")
        self._kernel_size = setting["kernel_size"]
        if self._kernel_size % 2 == 0 or self._kernel_size > 100 or (self._kernel_size < 1 and self._kernel_size != -1):
            raise RuntimeError("カーネルサイズは-1、1～99の奇数である必要がある")

    def apply(self, img: np.ndarray):
        return ((abs(cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=self._kernel_size)) +
                 abs(cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=self._kernel_size))) / 2).astype('uint8')

    def description(self):
        return "カーネルサイズ: {}".format(self._kernel_size)

    def generate_code(self):
        comment = "Scharrフィルタ" if self._kernel_size == -1 else "Sobelフィルタ"
        return "# {comment}\nimg = ((abs(cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize={kernel_size})) + abs(cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize={kernel_size}))) // 2).astype('uint8')".format(
            kernel_size=self._kernel_size, comment=comment)

    @staticmethod
    def overview() -> str:
        return "エッジ検出フィルタ"

    @staticmethod
    def method_name() -> str:
        return "sobel"

    @staticmethod
    def args_info() -> List[ArgInfo]:
        return [
            ArgInfo("kernel_size", "odd int", "カーネルサイズ　-1にすることでscharrフィルタになる"),
        ]
