from selenium.webdriver.common.by import By

from .base_page import BasePage, D
from .element import Element


class PageLogin(BasePage):

    url = '/'

    login_field = D(Element((By.ID, "login")))
    password_field = D(Element((By.ID, "passwd")))
    login_button = D(Element((By.ID, "submit")))
