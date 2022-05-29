import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By                # for locators


class DemoNopCommerce:

    #URL
    URL_NOP = "https://demo.nopcommerce.com/"

    #Locators
    LOGIN_TEXT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
    USER_FIELD = (By.CSS_SELECTOR, '#Email')
    PASS_FIELD = (By.NAME, 'Password')
    LOGIN_BUTTON = (By.XPATH, '//div/button[@type="submit"]')
    APPAREL = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/a')
    SHOES = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[1]/a')
    CLOTHING = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[2]/a')
    ACCESSORIES = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[3]/a')


    #Initializer
    def __init__(self, browser):        # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser          # instance attributes

    # Instance Interaction methods
    def loadPage(self):
        self.browser.get(self.URL_NOP)

    def get_InfoLogin(self):
        login_text = self.browser.find_element(*self.LOGIN_TEXT).text
        print("\nAction: ", login_text)
        print("\n ---", self.browser.title)
        print(" ---", self.browser.current_url)
        print(" ---", self.browser.page_source)

        self.browser.quit()

    def getLogin(self):
        self.browser.maximize_window()
        self.browser.find_element(*self.LOGIN_TEXT).click()

        self.browser.find_element(*self.USER_FIELD).send_keys("tantamarasescu@yahoo.com")  # create your own
        self.browser.find_element(*self.PASS_FIELD).send_keys("Admin123!")                 # create your own
        self.browser.find_element(*self.LOGIN_BUTTON).click()

        apparel = self.browser.find_element(*self.APPAREL)
        shoes = self.browser.find_element(*self.SHOES)
        clothing = self.browser.find_element(*self.CLOTHING)
        accessories = self.browser.find_element(*self.ACCESSORIES)

        actions = ActionChains(self.browser)
        actions.move_to_element(apparel).move_to_element(shoes).move_to_element(clothing).move_to_element(accessories).click().perform()

        time.sleep(3)

        self.browser.quit()


