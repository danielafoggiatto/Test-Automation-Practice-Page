from selenium.webdriver.common.by import By


def test_CT001_login_valido(driver):
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "login-button").click()

    login_sucessful = driver.find_element(By.ID, "login-status")
    assert login_sucessful.text == "Login successful!"