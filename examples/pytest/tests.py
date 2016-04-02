def test_login(horizon, steps):
    # steps.login(horizon.current_page, login='admin', password='admin')
    steps.logout(horizon.current_page)
