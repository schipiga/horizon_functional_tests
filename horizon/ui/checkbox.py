from .base import Ui, immediately


class CheckBox(Ui):

    @property
    @immediately
    def is_cheched(self):
        return self._web_element.is_selected()

    def check(self):
        if not self.is_cheched:
            self.click()

    def uncheck(self):
        if self.is_cheched:
            self.click()
