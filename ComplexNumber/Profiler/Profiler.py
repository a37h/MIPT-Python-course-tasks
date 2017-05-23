import time
import sys
import functools


def profiler(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        if wrapped.startTime != 0:
            wrapped.flag = 1
        else:
            wrapped.startTime = time.time()
            wrapped.calls = 0
        wrapped.calls += 1
        if wrapped.flag:
            return function(*args, **kwargs)
        result = function(*args, **kwargs)
        wrapped.last_time_taken = (time.time() - wrapped.startTime)
        wrapped.startTime = 0
        wrapped.flag = 0
        return result
    wrapped.calls = 0
    wrapped.flag = 0
    wrapped.startTime = 0
    return wrapped


exec(sys.stdin.read())
