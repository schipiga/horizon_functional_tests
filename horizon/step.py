from .config import Config


class DummyStep(object):

    def __init__(self, msg):
        pass

    def __enter__(self):
        pass

    def __exit__(self, ex_type, ex_value, ex_tb):
        pass

    def __call__(self, func):
        return func


class Step(object):

    def __init__(self, message):
        self._message = message

    def __enter__(self):
        self._step.__enter__()

    def __exit__(self, ex_type, ex_value, ex_tb):
        self._step.__exit__(ex_type, ex_value, ex_tb)

    def __call__(self, func):
        def wrapper(*args, **kwgs):
            return self._step(func)(*args, **kwgs)
        return wrapper

    @property
    def _step(self):
        if not getattr(self, '_cached_step', None):
            self._cached_step = (Config.step or DummyStep)(self._message)
        return self._cached_step
