from selenium.webdriver.common.by import By
import pytest

@pytest.mark.iframe
def test_CT010_iframe(driver):
    iframe1 = driver.find_element(By.XPATH, "//*[text()='iFrame Test']")

    iframe2 = driver.find_element(By.ID, "test-iframe")
    driver.switch_to.frame(iframe2)

    link = driver.find_element(By.XPATH, "//*[text()='More information...']")

    assert link.is_displayed() 