from functools import wraps

from horizon.config import Config


def cached(func):

    @wraps(func)
    def wrapper(self, *args, **kwgs):
        attr_name = '_cached_' + func.__name__
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self, *args, **kwgs))
        return getattr(self, attr_name)

    return wrapper


def immediately(func):

    @wraps(func)
    def wrapper(ui, *args, **kwgs):
        try:
            ui.web_driver.implicitly_wait(0)
            return func(ui, *args, **kwgs)
        finally:
            ui.web_driver.implicitly_wait(Config.ui_wait)

    return wrapper


def must_defined(func):

    @wraps(func)
    def wrapper(*args, **kwgs):
        result = func(*args, **kwgs)
        if result is None:
            raise AttributeError(
                "{} isn't defined".format(func.__name__.capitalize()))
        return result

    return wrapper


class ContainerMixin(object):

    def find_element(self, locator):
        return self.web_element.find_element(*locator)

    def find_elements(self, locator):
        return self.web_element.find_elements(*locator)
