from typing import List, Dict


def float_validation(value: str or float or int, min_val: float, max_val: float, variable_name: str):
    if not isinstance(value, float) and not isinstance(value, int):
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の小数である必要がある.")
    if value > max_val or value < min_val:
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の小数である必要がある.")


def int_validation(value: str or int, min_val: int, max_val: float, variable_name: str):
    if not isinstance(value, float) and not isinstance(value, int):
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の整数である必要がある.")
    if value > max_val or value < min_val:
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の整数である必要がある.")


def odd_validation(value: str or int, min_val: int, max_val: float, variable_name: str):
    if not isinstance(value, float) and not isinstance(value, int):
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の奇数である必要がある.")
    if value % 2 == 0 or value > max_val or value < min_val:
        raise RuntimeError(f"{variable_name}は{min_val}～{max_val}の奇数である必要がある.")


def dict_key_validation(dict_val: Dict[str, any], keys: List[str], variable_name: str):
    for key in keys:
        if dict_val.get(key) is None:
            raise RuntimeError(f"{variable_name}は {','.join(keys)} が必要")
