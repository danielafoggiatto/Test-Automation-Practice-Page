from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.modal
def test_CT012_modal(driver):
    driver.find_element(By.ID, "open-modal").click()

    message = driver.find_element(By.XPATH, "//*[text()='This is a modal window.']")

    assert message.text == "This is a modal window." 
    
    fechar_modal = driver.find_element(By.ID, "close-modal")
    fechar_modal.click()

    WebDriverWait(driver, 10).until(
    EC.invisibility_of_element(message)
    )