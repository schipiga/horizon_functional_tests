from horizon.step import Step

__all__ = ['logout']


@Step('logout')
def logout(page):
    page.logout_button.click()
