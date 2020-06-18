import cv2
import numpy as np
from django.conf import settings
from pathlib import Path
from .utils import *
from PIL import Image


def clear_images_regularly():
    media_path = settings.MEDIA_ROOT
    allowed_file_count = settings.ALLOWED_FILTER_FILE_COUNT
    sorted_filepaths = calc_sorted_filepaths(media_path)
    for filepath in sorted_filepaths[:-allowed_file_count]:
        os.remove(filepath)


def uploaded_file_name(file) -> str:
    return file.name


def uploaded_file_to_cvimage(file) -> np.ndarray:
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    if image.ndim == 2:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return image


def save_image(file_path: str, image: np.ndarray):
    if not Path(settings.MEDIA_ROOT).exists():
        Path(settings.MEDIA_ROOT).mkdir()
    # PILに合わせる
    if image.ndim == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    elif image.ndim == 4:
        cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)
    Image.fromarray(image).save(f"{settings.MEDIA_ROOT}/{file_path}")


@async_func
def save_image_async(file_path: str, image: np.ndarray):
    save_image(file_path, image)


def generate_filepath_for_display(filename: str) -> str:
    return "{}/{}".format(settings.MEDIA_URL, filename)
