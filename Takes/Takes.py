import functools
import sys


def takes(*types):
    def wrapped(func):
        @functools.wraps(func)
        def box(*args):
            for argument, type_ in zip(args, types):
                if not isinstance(argument, type_):
                    raise TypeError

            return func(*args)

        return box

    return wrapped


exec(sys.stdin.read())
