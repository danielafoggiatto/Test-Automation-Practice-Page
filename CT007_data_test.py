from selenium.webdriver.common.by import By
import pytest

@pytest.mark.data
def test_CT007_data(driver):
    data = driver.find_element(By.ID, "date-picker")
    data.send_keys("18/12/1992")

    valor = data.get_attribute("value")
    assert valor == "1992-12-18"
    