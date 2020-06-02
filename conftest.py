import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def language(request):
    language = request.config.getoption("language")
    return language
