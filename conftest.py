import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os

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
        os.system("pkill -x '" + request.param + "'")
        driver.quit()

    request.addfinalizer(driver_teardown)
    return driver