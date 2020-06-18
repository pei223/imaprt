import cv2
import numpy as np
from django.conf import settings
from pathlib import Path
from .utils import *


def clear_images_regularly():
    media_path = settings.MEDIA_ROOT
    allowed_file_count = settings.ALLOWED_FILTER_FILE_COUNT
    sorted_filepaths = calc_sorted_filepaths(media_path)
    for filepath in sorted_filepaths[:-allowed_file_count]:
        os.remove(filepath)


def uploaded_file_name(file) -> str:
    return file.name


def uploaded_file_to_cvimage(file) -> np.ndarray:
    return cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)


def save_image(file_path: str, image: np.ndarray):
    if not Path(settings.MEDIA_ROOT).exists():
        Path(settings.MEDIA_ROOT).mkdir()
    cv2.imwrite(f"{settings.MEDIA_ROOT}/{file_path}", image)


def generate_filepath_for_display(filename: str) -> str:
    return "{}/{}".format(settings.MEDIA_URL, filename)
