__all__ = ["PageKeyPairs", "PageMain"]


class WebElement(object):

    def set_text(self, text):
        pass

    def get_text(self, text):
        pass

    def click(self):
        pass

    def right_click(self):
        pass

    def double_click(self):
        pass

    @property
    def is_present(self):
        pass

    @property
    def is_checked(self):
        pass

    @property
    def is_enabled(self):
        pass

    @property
    def is_visible(self):
        pass

    @property
    def name(self):
        pass

    @property
    def position(self):
        pass



class Element(object):

    def __init__(self, selector):
        self._selector = selector
        self._element = None

    @property
    def _selenium_selector(self):
        return self._selector.split(':', 1)

    def __get__(self, page, page_type=None):
        if self._element:
            try:
                self._element.is_displayed()
            except Exception:
                self._element = page.webdriver.find_element(*self._selenium_selector)
        else:
            self._element = page.webdriver.find_element(*self._selenium_selector)
        return self._element


class BasePage(object):

    def __init__(self, webdriver):
        self.webdriver = webdriver


class PageKeyPairs(BasePage):

    url = '/project/keypairs'

    create_keypair_button = Element("id:create_keypair")
    import_keypair_button = Element("id:import_keypair")
    keypair_name_field = Element("id:name")
    public_key_field = Element("id:public_key")


class PageMain(BasePage):

    url = '/'

    login_field = Element("name:login")
    password_field = Element("name:passwd")
    login_button = Element("name:submit")
