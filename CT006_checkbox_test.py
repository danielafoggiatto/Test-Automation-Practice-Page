import pytest
from selenium.webdriver.common.by import By

@pytest.mark.feature
def test_CT006_checkbox_feature(driver):
    feature1 = driver.find_element(By.XPATH, "//*[@value='feature1']")
    feature1.click()
    
    feature2 = driver.find_element(By.XPATH, "//*[@value='feature2']")
    feature2.click()
    
    assert feature2.is_selected() and feature1.is_selected() == True


@pytest.mark.option
def test_CT006_checkbox_feature(driver):
    optionA = driver.find_element(By.XPATH, "//*[@value='optionA']")
    optionA.click()

    optionB = driver.find_element(By.XPATH, "//*[@value='optionB']")
    optionB.click()

    assert optionA.is_selected() or optionB.is_selected() == True