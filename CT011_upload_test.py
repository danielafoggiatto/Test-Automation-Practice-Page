from selenium.webdriver.common.by import By
import pytest

@pytest.mark.upl
def test_CT011_upload(driver):
    file_path = r"C:\Users\danie\OneDrive\Imagens\Screenshots\Captura de tela 2025-08-25 164540.png"
    
    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(file_path)
    
    uploaded = driver.find_element(By.XPATH, "//*[text()='Selected File: Captura de tela 2025-08-25 164540.png']")

    assert uploaded.text == "Selected File: Captura de tela 2025-08-25 164540.png"