import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators as LL

from data import Urls, UserData, TIME_WAIT


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.main_page)

    yield driver
    driver.quit()
