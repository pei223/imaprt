import numpy as np
import cv2

from . import BaseFilter


class Origin(BaseFilter):
    def apply(self, img: np.ndarray):
        return img

    def description(self):
        return "元画像"

    def generate_code(self):
        return ""
