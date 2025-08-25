from selenium.webdriver.common.by import By
import pytest

@pytest.mark.opt
def test_CT004_option_selection(driver):
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.common.by import By

    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    dropdown.select_by_value("option3")

    selected_option = dropdown.first_selected_option
    
    assert selected_option.get_attribute("value") == "option3"
