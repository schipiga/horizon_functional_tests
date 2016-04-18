from .base import Ui


class TextField(Ui):

    def set_text(self, text):
        self._web_element.send_keys(text)

    @property
    def text(self):
        return self._web_element.text
