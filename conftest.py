import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

CLOSE_BUTTON_XPATH = "/AXApplication[@AXTitle='Calculator']/AXWindow[@AXIdentifier='_NS:435' and @AXSubrole='AXStandardWindow']/AXButton[@AXSubrole='AXCloseButton']"

@pytest.fixture(scope='module')
def driver(request):
    desiredCapabilities = {
        'platformName': 'mac',
        'automationName': 'Mac'
    }

    driver = webdriver.Remote(
        command_executor='http://localhost:4723/wd/hub',
        desired_capabilities=desiredCapabilities
    )

    driver.get(request.param)

    def driver_teardown():
        driver.find_element(by=AppiumBy.XPATH, value=CLOSE_BUTTON_XPATH).click()
        driver.quit()

    request.addfinalizer(driver_teardown)
    return driver