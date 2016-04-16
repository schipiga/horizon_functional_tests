import abc
from functools import wraps

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import config


__all__ = ["PageKeyPairs", "PageMain"]


class IElement(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_text(self, text):
        """
        """

    @abc.abstractproperty
    def text(self):
        """
        """

    @abc.abstractmethod
    def click(self):
        """
        """

    @abc.abstractmethod
    def right_click(self):
        """
        """

    @abc.abstractmethod
    def double_click(self):
        """
        """

    @abc.abstractproperty
    def is_present(self):
        """
        """

    @abc.abstractproperty
    def is_checked(self):
        """
        """

    @abc.abstractproperty
    def is_enabled(self):
        """
        """

    @abc.abstractproperty
    def is_visible(self):
        """
        """


class IClonable(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def clone(self, *args, **kwgs):
        """Clone object.
        """


def immediately(func):

    @wraps(func)
    def wrapper(element, *args, **kwgs):
        try:
            element.webdriver.implicitly_wait(0)
            return func(element, *args, **kwgs)
        finally:
            element.webdriver.implicitly_wait(config.element_wait)

    return wrapper


def cache(func):

    @wraps(func)
    def wrapper(self, *args, **kwgs):
        attr_name = '_cached_' + func.__name__
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self, *args, **kwgs))
        return getattr(self, attr_name)

    return wrapper


class Element(IElement, IClonable):

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


class D(object):

    def __init__(self, element):
        self._element = element
        self._cache = {}

    def __get__(self, page, objtype=None):
        page_id = id(page)
        if page_id not in self._cache:
            self._cache[page_id] = self._element.clone(page=page)
        return self._cache[page_id]


class BasePage(object):

    def __init__(self, app):
        self.app = app
        self.webdriver = app.webdriver


class PageKeyPairs(BasePage):

    url = '/project/keypairs'

    create_keypair_button = D(Element((By.ID, "create_keypair")))
    import_keypair_button = D(Element((By.ID, "import_keypair")))
    keypair_name_field = D(Element((By.ID, "name")))
    public_key_field = D(Element((By.ID, "public_key")))


class PageMain(BasePage):

    url = '/'

    login_field = D(Element((By.ID, "login")))
    password_field = D(Element((By.ID, "passwd")))
    login_button = D(Element((By.ID, "submit")))
