from horizon.interfaces import IClonable, IUi, IWeb
# TODO seems they must be defined here
from horizon.utils import ContainerMixin, cached, immediately, must_defined

from selenium.webdriver import ActionChains


def register_ui(**kwgs):

    def wrapper(cls):
        cls.register_ui(kwgs)
        return cls

    return wrapper


class Ui(IUi, IWeb, IClonable, ContainerMixin):

    def __init__(self, locator, container=None):
        self.locator = locator
        self._container = container

    def click(self):
        self.web_element.click()

    def right_click(self):
        self._action_chains.context_click(self.web_element).perform()

    def double_click(self):
        self._action_chains.double_click(self.web_element).perform()

    @property
    @immediately
    def is_present(self):
        try:
            self.web_element.is_displayed()
            return True
        except Exception:
            return False

    @property
    @immediately
    def is_enabled(self):
        return self.web_element.is_enabled()

    @property
    @immediately
    def is_visible(self):
        return self.web_element.is_displayed()

    @property
    @cached
    def web_driver(self):
        return self.container.web_driver

    @property
    @cached
    def web_element(self):
        self.container.find_element(self.locator)

    @property
    @cached
    def _action_chains(self):
        return ActionChains(self.web_driver)

    @property
    @must_defined
    def container(self):
        return self._container

    def clone(self, locator=None, container=None):
        return type(self)(locator or self.locator, container or self.container)
