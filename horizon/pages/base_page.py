from selenium.webdriver.common.by import By

from horizon.interfaces import IPage, IWeb
from horizon.utils import ContainerMixin


class BasePage(IPage, IWeb, ContainerMixin):

    def __init__(self, app):
        self.app = app
        self.locator = (By.TAG_NAME, 'html')
        self.web_driver = app.web_driver
        self.web_element = self.web_driver.find_element(*self.locator)
