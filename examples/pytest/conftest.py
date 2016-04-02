import horizon.steps as horizon_steps
import pytest
from horizon import Horizon
from horizon.config import Config


Config.screencapture = True


@pytest.yield_fixture(scope='session')
def horizon():
    horizon = Horizon('http:/localhost:8000', 'firefox')
    horizon.open_page_main()
    yield horizon
    horizon.quit()


@pytest.fixture(scope='session')
def steps():
    return horizon_steps
