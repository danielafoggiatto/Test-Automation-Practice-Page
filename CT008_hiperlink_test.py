from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.link
def test_CT008_hiperlink(driver):
    newtab = driver.find_element(By.ID, "test-link").click()

    time.sleep(1)
    abas = driver.window_handles

    driver.switch_to.window(abas[-1])

    novo_link = driver.find_element(By.XPATH, "//*[text()='More information...']").click()

    assert driver.title == "Example Domains"


