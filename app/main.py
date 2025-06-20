from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    _cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        if args in _cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            _cache[args] = func(*args, **kwargs)
        return _cache[args]
    return wrapper
