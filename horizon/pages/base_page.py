from horizon.interfaces import IPage, IWebdriverable


class D(object):

    def __init__(self, element):
        self._element = element
        self._cache = {}

    def __get__(self, page, objtype=None):
        page_id = id(page)
        if page_id not in self._cache:
            self._cache[page_id] = self._element.clone(page=page)
        return self._cache[page_id]


class BasePage(IPage, IWebdriverable):

    def __init__(self, app):
        self.app = app
        self.webdriver = app.webdriver
