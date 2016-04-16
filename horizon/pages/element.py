from functools import wraps

from selenium.webdriver import ActionChains

from horizon.config import Config
from horizon.interfaces import IElement, IClonable, IWebdriverable
from horizon.utils import cache


def immediately(func):

    @wraps(func)
    def wrapper(element, *args, **kwgs):
        try:
            element.webdriver.implicitly_wait(0)
            return func(element, *args, **kwgs)
        finally:
            element.webdriver.implicitly_wait(Config.element_wait)

    return wrapper


class Element(IElement, IClonable, IWebdriverable):

    def __init__(self, locator, page=None):
        self._locator = locator
        self._page = page
        self._cached_web_element = None

    @property
    @cache
    def webdriver(self):
        if not self._page:
            raise AttributeError("Page isn't specified")
        return self._page.webdriver

    @property
    @cache
    def _action_chains(self):
        return ActionChains(self.webdriver)

    @property
    @cache
    def _web_element(self):
        return self.webdriver.find_element(*self._locator)

    def set_text(self, text):
        self._web_element.send_keys(text)

    @property
    def text(self):
        return self._web_element.text

    def click(self):
        self._web_element.click()

    def right_click(self):
        self._action_chains.context_click(self._web_element).perform()

    def double_click(self):
        self._action_chains.double_click(self._web_element).perform()

    @property
    @immediately
    def is_present(self):
        try:
            self._web_element.is_displayed()
            return True
        except Exception:
            return False

    @property
    @immediately
    def is_cheched(self):
        return self._web_element.is_selected()

    @property
    @immediately
    def is_enabled(self):
        return self._web_element.is_enabled()

    @property
    @immediately
    def is_visible(self):
        return self._web_element.is_displayed()

    def clone(self, locator=None, page=None):
        return type(self)(locator or self._locator, page or self._page)
