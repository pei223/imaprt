from typing import Tuple, List
import numpy as np

from ... import media_manager
from . import *


def apply_chain_filtering(image: np.ndarray, origin_image_name: str, filtering_ls: List[BaseFilter]) -> \
        Tuple[List[FilterImageInfo], CodeGenerator]:
    """
    フィルタを重ねる処理実行
    :param image: 元画像
    :param origin_image_name: 元画像の名前
    :param filtering_ls: フィルタリング手法リスト
    :return: フィルタ適用された画像の情報, コード生成器
    """
    code_generator = CodeGenerator()
    filter_image_info_ls = []
    for i, filtering in enumerate(filtering_ls):
        filter_image_info = FilterImageInfo(origin_image_name, i, filtering)
        image = filtering.apply(image)
        media_manager.save_image(filter_image_info.new_filename, image)
        filter_image_info_ls.append(filter_image_info)
        code_generator.add(filtering.generate_code())
    return filter_image_info_ls, code_generator


def apply_batch_filtering(origin_image: np.ndarray, origin_image_name: str, filtering_ls: List[BaseFilter]) -> \
        Tuple[List[FilterImageInfo], CodeGenerator]:
    """
    フィルタを一括適用する処理実行
    :param origin_image: 元画像
    :param origin_image_name: 元画像の名前
    :param filtering_ls: フィルタリング手法リスト
    :return: フィルタ適用された画像の情報, コード生成器
    """
    code_generator = CodeGenerator()
    filter_image_info_ls = []
    for i, filtering in enumerate(filtering_ls):
        filter_image_info = FilterImageInfo(origin_image_name, i, filtering)
        image = filtering.apply(origin_image)
        media_manager.save_image(filter_image_info.new_filename, image)
        filter_image_info_ls.append(filter_image_info)
        code_generator.add(filtering.generate_code())
    return filter_image_info_ls, code_generator
