from threading import Thread


# 関数を非同期化するデコレータ
def async_func(func):
    def wrapper(*args, **kwargs):
        func_hl = Thread(target=func, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl

    return wrapper
