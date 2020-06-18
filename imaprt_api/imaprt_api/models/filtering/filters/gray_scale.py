import cv2
import numpy as np

from .base_filter import BaseFilter


class GrayScale(BaseFilter):
    def apply(self, img: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def description(self):
        return "グレースケール"

    def generate_code(self):
        return "# グレースケール\nimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)"
