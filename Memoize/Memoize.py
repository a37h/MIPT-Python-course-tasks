import sys
import functools


def memoize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arguments = args + tuple(kwargs.items())
        if arguments not in wrapper.cache:
            wrapper.cache[arguments] = func(*args, **kwargs)
        return wrapper.cache[arguments]

    wrapper.cache = {}
    return wrapper


exec(sys.stdin.read())
