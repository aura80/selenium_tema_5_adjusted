from selenium.webdriver.common.by import By


class Locators:

    # Locators
    SEARCH_CSS = (By.CSS_SELECTOR, 'input.wikipedia-search-input')
    SEARCH_TEXT = (By.XPATH, '//input[@id="Wikipedia1_wikipedia-search-input"]')
    SEARCH_FULLXPATH = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[1]/div[1]/form/div/span[2]/span[1]/input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input.wikipedia-search-button')
    COOKIE_BUTTON = (By.CSS_SELECTOR, 'a#cookieChoiceDismiss')
    ALL_SEARCH_RESULTS = (By.XPATH, '//div[@id="Wikipedia1_wikipedia-search-results"]//a')
    SEARCH_ONE = (By.XPATH, '//a[text()="Blogger"]')
    SEARCH_TWO = (By.XPATH, '//div[@id="Wikipedia1_wikipedia-search-results"]//div[@id="wikipedia-search-result-link"]/a')
    ACTIONS = (By.CSS_SELECTOR, '.widget  h2[class="title"]')
    ALERT_TEXT = (By.CSS_SELECTOR, '.column-left-inner .sidebar .widget:nth-child(2) h2')
    ALERT_POPUP = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    ALERT_MSG = (By.CSS_SELECTOR, 'p#demo')
    DATE_PICKER = (By.XPATH, '//input[@id="datepicker"]')
    DATE_SELECT = (By.CSS_SELECTOR, 'td a.ui-state-default.ui-state-highlight')
    DATE_MONTH = (By.CSS_SELECTOR, '.ui-datepicker-month')
    DATE_YEAR = (By.CSS_SELECTOR, '.ui-datepicker-year')
    DATE_NEW = (By.LINK_TEXT, '25')
    LINKS_PAGE = (By.XPATH, "//div[@class='div a']//a")
    IFRAME_TAG = (By.TAG_NAME, "iframe")
    FIRST_NAME = (By.CSS_SELECTOR, '#RESULT_TextField-1')
    LAST_NAME = (By.CSS_SELECTOR, '#RESULT_TextField-2')
    PHONE_NO = (By.NAME, 'RESULT_TextField-3')
    COUNTRY = (By.NAME, 'RESULT_TextField-4')
    CITY = (By.NAME, 'RESULT_TextField-5')
    EMAIL = (By.NAME, 'RESULT_TextField-6')
    MALE_BUTTON = (By.XPATH, '//label[@for="RESULT_RadioButton-7_0"]')
    FEMALE_BUTTON = (By.XPATH, '//label[@for="RESULT_RadioButton-7_1"]')
    VOLUNTEER = (By.CSS_SELECTOR, '#q19 h1')
    CATEGORY = (By.CSS_SELECTOR, 'div .q .question.top_question')
    DAYS = (By.CSS_SELECTOR, '#q15.q  td label')
    BEST_TIME = (By.CSS_SELECTOR, '#RESULT_RadioButton-9')
    SUBMIT = (By.XPATH, '//input[@id="FSsubmit"]')
    TABLE_HEAD = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[1]/th')
    FIRST_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[2]/td')
    SECOND_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[3]/td')
    THIRD_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[4]/td')
    TABLE_ROWS = (By.XPATH, '//table[@name="BookTable"]//tr')
    TABLE_COL = (By.XPATH, '//table[@name="BookTable"]//tr[1]/th')
    ALL_CELLS = (By.XPATH, '//table[@name="BookTable"]/tbody/tr["+str(i)+"]/td["+str(j)+"]')
    DOUBLE_CLICK_ONE = (By.XPATH, '//input[@id="field1"]')
    DOUBLE_CLICK_TWO = (By.XPATH, '//input[@id="field2"]')
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[ondblclick="myFunction1()"]')
    DRAG_ELEM = (By.ID, 'draggable')
    DROP_ELEM = (By.ID, 'droppable')
    SLIDER = (By.CSS_SELECTOR, 'span.ui-slider-handle.ui-corner-all.ui-state-default')
    ALL_IMG_AMAZON = (By.TAG_NAME, 'img')

    list_loc = [COOKIE_BUTTON, SEARCH_BUTTON, SEARCH_CSS, ALL_SEARCH_RESULTS, SEARCH_ONE, SEARCH_TEXT, SEARCH_TWO, ALERT_TEXT, ALERT_POPUP, ALERT_MSG,
                DATE_PICKER, DATE_SELECT, DATE_MONTH, DATE_YEAR, DATE_NEW, IFRAME_TAG, VOLUNTEER, CATEGORY, FIRST_NAME, LAST_NAME, PHONE_NO, COUNTRY,
                CITY, EMAIL, MALE_BUTTON, DAYS, BEST_TIME, SUBMIT, TABLE_ROWS, TABLE_COL, TABLE_HEAD, FIRST_ROW, SECOND_ROW, THIRD_ROW, DOUBLE_CLICK_ONE,
                DOUBLE_CLICK_BUTTON, DRAG_ELEM, DROP_ELEM, SLIDER, ALL_IMG_AMAZON]