from selenium.webdriver.common.by import By

from horizon.ui import Button, TextField, register_ui

from .base_page import BasePage


@register_ui(login_field=TextField((By.ID, "login")),
             password_field=TextField((By.ID, "passwd")),
             login_button=Button((By.ID, "submit")))
class PageLogin(BasePage):
    url = '/'
