from abc import ABCMeta, abstractmethod
from typing import List

import numpy as np
from ..help import ArgInfo


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

    @staticmethod
    @abstractmethod
    def overview() -> str:
        pass

    @staticmethod
    @abstractmethod
    def method_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def args_info() -> List[ArgInfo]:
        pass
