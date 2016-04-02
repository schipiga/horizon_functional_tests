import horizon.steps as steps
from horizon import Horizon
from testtools import TestCase


class HorizonMixin(object):

    def setUp(self):
        super(HorizonMixin, self).setUp()
        self.horizon = Horizon('https://localhost:8000', 'firefox')
        self.horizon.open_page_main()

    def tearDown(self):
        self.horizon.quit()
        super(HorizonMixin, self).tearDown()


class TestHorizon(HorizonMixin, TestCase):

    def test_login(self):
        steps.login(self.horizon.current_page, login='admin', password='admin')
