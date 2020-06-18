from abc import ABCMeta, abstractmethod
from typing import List, Dict

import numpy as np
import cv2


class BaseFilter(metaclass=ABCMeta):
    @abstractmethod
    def apply(self, img: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def generate_code(self) -> str:
        pass
