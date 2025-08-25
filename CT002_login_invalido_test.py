from selenium.webdriver.common.by import By
import pytest

@pytest.mark.invalido
def test_CT002_login_invalido(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1111")
    driver.find_element(By.ID, "login-button").click()

    login_invalido = driver.find_element(By.ID, "login-status")

    assert login_invalido.text == "Incorrect username or password."