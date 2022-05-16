import time
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from pages.switch_emag_page import emag


class amazon(emag):

    #URL
    URL3 = "https://www.amazon.com/"

    # #Locators
    AMAZON_SEARCH = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
    AMAZON_CLICK = (By.CSS_SELECTOR, '#nav-search-submit-button')


    #Initializer
    def __init__(self, browser):            # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser              # instance attributes
        super().__init__(browser)           # calls base class emag
        self.browser.get(self.URL3)


    def get_Navi(self):
        self.browser.maximize_window()

        emag(self.browser)

        self.browser.back()


        self.browser.find_element(*self.AMAZON_SEARCH).send_keys("pet")

        timp = WebDriverWait(self.browser, 10, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception])
        timp.until(EC.presence_of_element_located(self.AMAZON_CLICK)).click()

        self.browser.forward()

        time.sleep(3)

        self.browser.refresh()
        time.sleep(2)

        self.browser.quit()


    def get_Links(self):
        self.browser.maximize_window()

        self.browser.get(self.URL3)

        all_img = self.browser.find_elements(By.TAG_NAME, 'img')    #By.TAG_NAME, 'img'         *self.list_loc[41]
        print("\nTotal no. of img on amazon: ", len(all_img))

        broken, ok = 0, 0
        for img in range(len(all_img)):
            url = all_img[img].get_attribute('src')

            try:
                cerere = requests.head(url)
            except:
                None

            if cerere.status_code >= 400:
                print(f'Link {img} broken: ', url)
                broken += 1
            else:
                print(f'Link {img} ok: ', url)
                ok += 1

        print("Total no. of broken amazon links: ", broken)
        print("Total no. of ok amazon links: ", ok)

        self.browser.quit()


