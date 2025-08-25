from selenium.webdriver.common.by import By
import pytest

@pytest.mark.vazio
def test_CT003_login_campo_vazio(driver):
    driver.find_element(By.ID, "login-button").click()

    username = driver.find_element(By.ID, "username")
    validation_message = username.get_attribute("validationMessage")

    print(validation_message) 
    assert validation_message == "Preencha este campo."
