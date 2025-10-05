from appium.webdriver.common.appiumby import AppiumBy
import random
import pytest

WINDOW_XPATH = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
RESULT_GROUP_XPATH = WINDOW_XPATH + "/AXGroup[0]"
BASIC_GROUP_XPATH = WINDOW_XPATH + "/AXGroup[1]"

@pytest.fixture
def clear_result(driver):
    driver.find_element(by=AppiumBy.XPATH, value=BASIC_GROUP_XPATH + "/AXButton[@AXDescription='clear']").click()

def get_random_num():
    return random.randint(0, 1000)

def type_num(driver, num):
    for digit in str(num):
        driver.find_element(by=AppiumBy.XPATH, value=BASIC_GROUP_XPATH + "/AXButton[@AXTitle='" + digit + "']").click()

@pytest.mark.parametrize("driver", ["Calculator"], indirect=["driver"])
@pytest.mark.parametrize('operator', ['add', 'subtract', 'multiply', 'divide'])
def test_calc(driver, clear_result, operator):
    first_num = get_random_num()
    type_num(driver, first_num)

    driver.find_element(by=AppiumBy.XPATH, value=BASIC_GROUP_XPATH + "/AXButton[@AXDescription='" + operator + "']").click()

    second_num = get_random_num()
    type_num(driver, second_num)

    driver.find_element(by=AppiumBy.XPATH, value=BASIC_GROUP_XPATH + "/AXButton[@AXDescription='equals']").click()

    text_result = driver.find_element(by=AppiumBy.XPATH, value=RESULT_GROUP_XPATH + "/AXStaticText[@AXDescription='main display']")

    if operator == 'add':
        assert int(text_result.text) == first_num + second_num
    elif operator == 'subtract':
        assert int(text_result.text) == first_num - second_num
    elif operator == 'multiply':
        assert int(text_result.text) == first_num * second_num
    elif operator == 'divide':
        if second_num != 0:
            assert round(float(text_result.text), 2) == round(first_num / second_num, 2)
        else:
            assert text_result.text == 'Not a number'