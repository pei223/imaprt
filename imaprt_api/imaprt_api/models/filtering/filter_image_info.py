from typing import Dict
from .filters import BaseFilter
from pathlib import Path
import hashlib
import time
from ... import media_manager


class FilterImageInfo:
    def __init__(self, origin_image_name: str, filter_order: int, filtering: BaseFilter):
        img_name_without_extension = Path(origin_image_name).stem
        suffix = Path(origin_image_name).suffix
        digest = self._generate_digest(img_name_without_extension)
        self.new_filename \
            = f"{img_name_without_extension}_{filtering.__class__.__name__}{filter_order}_{digest}{suffix}"
        self.filtering = filtering

    def _generate_digest(self, img_name_without_extension: str):
        return hashlib.sha256(f"{img_name_without_extension}{str(time.time())}".encode()).hexdigest()[:8]

    def to_dict(self) -> Dict:
        return {"filename": self.new_filename, "title": self.filtering.__class__.__name__,
                "description": self.filtering.description(),
                "url": media_manager.generate_filepath_for_display(self.new_filename)}
