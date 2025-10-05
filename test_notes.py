from appium.webdriver.common.appiumby import AppiumBy
import pytest

BASE_AXPATH = "/AXApplication[@AXTitle='Notes']/AXWindow[@AXTitle='Notes' and @AXSubrole='AXStandardWindow']"
SPLIT_GROUP_XPATH = BASE_AXPATH + "/AXSplitGroup[0]/AXSplitGroup[0]"
ADD_NOTE_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXButton[@AXDescription='New Note']"
DELETE_NOTE_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXButton[@AXDescription='Delete']"
NOTE_TEXTAREA_XPATH = SPLIT_GROUP_XPATH + "/AXGroup[0]/AXScrollArea[@AXIdentifier='Note Body Scroll View']/AXTextArea[@AXIdentifier='Note Body Text View']"
LIST_NOTES_XPATH = SPLIT_GROUP_XPATH + "/AXScrollArea/AXTable/AXRow/AXCell[0]/AXCell/AXStaticText"

@pytest.fixture
def delete_note(driver):
    yield
    driver.find_element(by=AppiumBy.XPATH, value=DELETE_NOTE_XPATH).click()

@pytest.mark.parametrize("driver", ["Notes"], indirect=["driver"])
def test_notes(driver, delete_note):
    NOTE_TITLE_TEXT = "New Note"

    driver.find_element(by=AppiumBy.XPATH, value=ADD_NOTE_XPATH).click()
    driver.find_element(by=AppiumBy.XPATH, value=NOTE_TEXTAREA_XPATH).send_keys(NOTE_TITLE_TEXT + "\n\nHere's some example text..")

    note_title = driver.find_element(by=AppiumBy.XPATH, value=LIST_NOTES_XPATH)
    assert note_title.text == NOTE_TITLE_TEXT
