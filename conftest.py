import pytest
from utils.driver_factory import create_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="chrome | firefox | edge")
    parser.addoption("--headless", action="store_true", default=None, help="Run browser headless")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    drv = create_driver(browser=browser, headless=headless)
    yield drv
    drv.quit()