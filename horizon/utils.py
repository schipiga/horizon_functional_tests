from functools import wraps


def cache(func):

    @wraps(func)
    def wrapper(self, *args, **kwgs):
        attr_name = '_cached_' + func.__name__
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self, *args, **kwgs))
        return getattr(self, attr_name)

    return wrapper
