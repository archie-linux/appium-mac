from appium.webdriver.common.appiumby import AppiumBy
import pytest

@pytest.mark.parametrize("driver", ["Activity Monitor"], indirect=["driver"])
def test_activity_monitor(driver):
    BASE_AXPATH = "/AXApplication[@AXTitle='Activity Monitor']/AXWindow"
    RADIO_BUTTON = BASE_AXPATH + "/AXToolbar/AXGroup[1]/AXRadioGroup/AXRadioButton[@AXTitle='{}']"

    driver.find_element(by=AppiumBy.XPATH, value=RADIO_BUTTON.format("Memory")).click()
    driver.find_element(by=AppiumBy.XPATH, value=RADIO_BUTTON.format("Energy")).click()
    driver.find_element(by=AppiumBy.XPATH, value=RADIO_BUTTON.format("Disk")).click()
    driver.find_element(by=AppiumBy.XPATH, value=RADIO_BUTTON.format("Network")).click()
    driver.find_element(by=AppiumBy.XPATH, value=RADIO_BUTTON.format("CPU")).click()

    serach_field = driver.find_element(by=AppiumBy.XPATH, value=BASE_AXPATH + "/AXToolbar/AXGroup/AXTextField[@AXSubrole='AXSearchField']")
    serach_field.send_keys("Activity Monitor")

    first_row = driver.find_element(by=AppiumBy.XPATH, value=BASE_AXPATH + "/AXScrollArea/AXOutline/AXRow[0]/AXStaticText")

    assert first_row.text == " Activity Monitor"