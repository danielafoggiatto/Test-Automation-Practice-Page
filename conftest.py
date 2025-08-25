from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Edge()

    driver.get("https://leogcarvalho.github.io/test-automation-practice/")

    yield driver

    driver.quit()