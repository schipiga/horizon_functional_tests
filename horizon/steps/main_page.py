from horizon.step import Step

__all__ = ['login']


def login(main_page, login, password):
    with Step('login as {!r} with password {!r}'.format(login, password)):
        main_page.login_field.send_keys(login)
        main_page.password_field.send_keys(password)
        main_page.login_button.click()
