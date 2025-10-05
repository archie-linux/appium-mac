from appium.webdriver.common.appiumby import AppiumBy
import pytest

BASE_AXPATH = "/AXApplication[@AXTitle='Notes']/AXWindow[@AXTitle='Notes' and @AXSubrole='AXStandardWindow']"
SPLIT_GROUP_XPATH = BASE_AXPATH + "/AXSplitGroup[0]/AXSplitGroup[0]/AXGroup[0]"
ADD_NOTE_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXButton[@AXDescription='New Note']"
DELETE_NOTE_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXButton[@AXDescription='Delete']"
NOTE_TEXTAREA_XPATH = SPLIT_GROUP_XPATH + "/AXScrollArea[@AXIdentifier='Note Body Scroll View']/AXTextArea[@AXIdentifier='Note Body Text View']"

ENTER_PASSWORD_TEXT_XPATH = BASE_AXPATH + "/AXSheet/AXStaticText[@AXValue='Enter the notes password to lock this note.'"
PASSWORD_LABEL_XPATH = BASE_AXPATH + "/AXSheet/AXStaticText[@AXValue='Password:']"
PASSWORD_TEXT_FIELD_XPATH = BASE_AXPATH + "/AXSheet/AXTextField[@AXSubrole='AXSecureTextField']"
PASSWORD_OK_XPATH = BASE_AXPATH + "/AXSheet/AXButton[@AXTitle='OK' and @AXIdentifier='PasswordSheetOK']"

LIST_NOTES_XPATH = BASE_AXPATH + "/AXSplitGroup[0]/AXSplitGroup[0]/AXScrollArea/AXTable/AXRow/AXCell[0]/AXCell/AXStaticText"
LOCK_NOTES_MENU_BUTTON_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXGroup[2]/AXMenuButton[@AXValue='locked']"
UNLOCK_NOTES_MENU_BUTTON_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXGroup[2]/AXMenuButton[@AXValue='unlocked']"
LOCK_NOTE_MENU_ITEM_BUTTON_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXGroup[2]/AXMenu[0]/AXMenuItem[@AXTitle='Lock Note']"
LOCK_WINDOW_XPATH = BASE_AXPATH + "/AXSheet"
CLOSE_ALL_LOCKED_NOTES_XPATH = BASE_AXPATH + "/AXToolbar[0]/AXGroup[2]/AXMenu[0]/AXMenuItem[@AXTitle='Close All Locked Notes]"

LOCK_ICON_XPATH = SPLIT_GROUP_XPATH
LOCKED_NOTE_TEXT_XPATH = SPLIT_GROUP_XPATH + "/AXStaticText[@AXValue='This note is locked.']"
LOCKED_NOTE_ENTER_PASSWORD_TEXT_XPATH = SPLIT_GROUP_XPATH + "/AXStaticText[@AXValue='Enter the notes password to view locked notes.']"
FIRST_NOTE_STATUS_XPATH = BASE_AXPATH +  "/AXSplitGroup[0]/AXSplitGroup[0]/AXScrollArea/AXTable/AXRow[@AXSubrole='AXTableRow']/AXCell[0]/AXCell/AXStaticText[@AXValue='Locked']"

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

@pytest.mark.parametrize("driver", ["Notes"], indirect=["driver"])
def test_lock_note(driver):
    NOTE_TITLE_TEXT = "New Note"

    # Create new note
    driver.find_element(by=AppiumBy.XPATH, value=ADD_NOTE_XPATH).click()
    driver.find_element(by=AppiumBy.XPATH, value=NOTE_TEXTAREA_XPATH).send_keys(NOTE_TITLE_TEXT + "\n\nHere's some example text..")

    # Lock Note
    driver.find_element(by=AppiumBy.XPATH, value=LOCK_NOTES_MENU_BUTTON_XPATH).click()
    driver.find_element(by=AppiumBy.XPATH, value=LOCK_NOTE_MENU_ITEM_BUTTON_XPATH).click()

    # Window to set lock password is displayed
    driver.find_element(by=AppiumBy.XPATH, value=LOCK_WINDOW_XPATH).is_displayed()

    enter_password_text =  driver.find_element(by=AppiumBy.XPATH, value=ENTER_PASSWORD_TEXT_XPATH)
    password_label = driver.find_element(by=AppiumBy.XPATH, value=PASSWORD_LABEL_XPATH)

    assert enter_password_text.text == 'Enter the notes password to lock this note.'
    assert password_label.text == 'Password:'

    driver.find_element(by=AppiumBy.XPATH, value=PASSWORD_TEXT_FIELD_XPATH).send_keys('1111')
    driver.find_element(by=AppiumBy.XPATH, value=PASSWORD_OK_XPATH).click()

    # Close locked notes
    driver.find_element(by=AppiumBy.XPATH, value=UNLOCK_NOTES_MENU_BUTTON_XPATH).click()
    driver.find_element(by=AppiumBy.XPATH, value=CLOSE_ALL_LOCKED_NOTES_XPATH).click()

    # Verify that the created note is locked
    cell_status = driver.find_element(by=AppiumBy.XPATH, value=FIRST_NOTE_STATUS_XPATH)
    assert cell_status.text == 'Locked'

    driver.find_element(by=AppiumBy.XPATH, value=LOCK_ICON_XPATH).is_displayed()
    driver.find_element(by=AppiumBy.XPATH, value=LOCKED_NOTE_TEXT_XPATH).is_displayed()
    driver.find_element(by=AppiumBy.XPATH, value=LOCKED_NOTE_ENTER_PASSWORD_TEXT_XPATH).is_displayed()

