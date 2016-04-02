from urlparse import urljoin

from selenium import webdriver

import pages


def snake_case(camel_case):
    return ''.join('_' + i.lower() if i.isupper() else i
                   for i in camel_case).strip('_')


def register_pages(pages):

    def wrapper(app):
        app.current_page = None

        for page in pages:

            def _open_page(self, page=page):
                self.open_url(page.url)
                self.current_page = page(self.webdriver)
                return self.current_page

            setattr(app, 'open_' + snake_case(page.__name__), _open_page)
        return app

    return wrapper


horizon_pages = map(
    lambda page_name: getattr(pages, page_name), pages.__all__)


browsers = {
    'firefox': webdriver.Firefox,
    'phantom': webdriver.PhantomJS,
    'Chrome': webdriver.Chrome,
}


@register_pages(horizon_pages)
class Horizon(object):

    browsers = browsers.keys()

    def __init__(self, url, browser, *args, **kwgs):
        self.app_url = url
        self.webdriver = browsers[browser](*args, **kwgs)
        self.webdriver.set_page_load_timeout(30)
        self.webdriver.get(url)

    def open_url(self, url):
        self.webdriver.get(urljoin(self.app_url, url))

    def quit(self):
        self.webdriver.quit()
