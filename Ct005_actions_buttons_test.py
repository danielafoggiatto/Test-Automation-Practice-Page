from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.alert
def test_CT005_action_buttons_alert(driver):
    driver.find_element(By.ID, "alert-button").click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present())
   
    alert_text = alert.text
    assert alert_text == "This is a test alert!"

    alert.accept()

    driver.find_element(By.ID, "color-button").click()

@pytest.mark.change
def test_CT005_action_buttons_change(driver):
    driver.find_element(By.ID, "color-button").click()

    body = WebDriverWait(driver, 5). until(lambda d: d.find_element(By.TAG_NAME, "body"))
    cor_body = body.value_of_css_property("background-color")

    assert cor_body == "rgba(173, 216, 230, 1)"