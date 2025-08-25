from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.hover
def test_CT009_hover(driver):
    menu = driver.find_element(By.XPATH, "//p[@class='menu-title']")

    ActionChains(driver).move_to_element(menu).perform()
    
    option2 = WebDriverWait(driver, 10).until(  EC.element_to_be_clickable((By.XPATH, "//a[@href='#option2']")))

    assert option2.is_displayed() == True