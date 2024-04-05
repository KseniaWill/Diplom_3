import pytest
from selenium import webdriver
from data import Urls


# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Firefox()
#     driver = webdriver.Chrome()
#     driver.get(Urls.main_page)
#
#     yield driver
#     driver.quit()
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.main_page)

    yield driver
    driver.quit()
