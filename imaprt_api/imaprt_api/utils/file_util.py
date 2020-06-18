import os
from typing import List


def calc_sorted_filepaths(dir_path: str, asc=True) -> List[str]:
    path_timestamp_ls = []
    for filename in os.listdir(dir_path):
        path = os.path.join(dir_path, filename)
        path_timestamp_ls.append((path, os.path.getmtime(path)))

    path_timestamp_ls = sorted(path_timestamp_ls, key=lambda x: x[1]) if asc else sorted(path_timestamp_ls,
                                                                                         key=lambda x: -x[1])
    return list(map(lambda x: x[0], path_timestamp_ls))
