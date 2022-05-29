import time
from datetime import datetime
from selenium.webdriver import ActionChains                         # for mouse actions
from selenium.webdriver.support.select import Select                # for selections ex dropdowns


from pages.locators import Locators


class AutomTestPracticePage(Locators):

    #URL
    URL = "https://testautomationpractice.blogspot.com/"

    # #Locators are in the class Locators

    #Initializer
    def __init__(self, browser):            # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser              # instance attributes

    # Instance Interaction methods
    def loadPage(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.list_loc[0]).click()

    def getSearch_Click(self):
        self.browser.find_element(*self.list_loc[1]).click()
        print("\n ---", self.browser.title)
        print(" ---", self.browser.current_url)

    def getTitle(self):
        print("\n", self.browser.title)
        assert self.browser.title == 'Automation Testing Practice', 'Title of the page was changed'

    def getWindowId(self):
        # it returns the current page id
        windowId = self.browser.current_window_handle
        print(f'\nThe ID of the page {self.browser.title} is:   {windowId}')
        self.browser.close()

    def getSearch_ByCSS(self):
        self.browser.find_element(*self.list_loc[2]).send_keys("Turism")
        obiect = AutomTestPracticePage
        obiect.getSearch_Click(self)

        self.browser.maximize_window()

        all_search_results = self.browser.find_elements(*self.list_loc[3])
        print(f'\nNo. of search results on \'{self.browser.title}\' page:  {len(all_search_results)}\n')

        # all the elements and hiperlinks received after searching
        for i in all_search_results:
            print(i.text, " - ", i.get_attribute('href'))

        time.sleep(2)

        self.browser.close()

    def getSearch_winID(self):
        self.browser.maximize_window()
        self.browser.find_element(*self.list_loc[4]).click()

        # it returns the id's of multiple browser windows
        windowId = self.browser.window_handles

        parent = windowId[0]
        child = windowId[1]

        # we have two windows only
        self.browser.switch_to.window(parent)
        print("\n   ID   ---  ", parent, "Title of the parent browser: ", self.browser.title)
        self.browser.switch_to.window(child)
        print("   ID   ---  ", child, "Title of the child browser: ", self.browser.title)

        time.sleep(2)

        self.browser.quit()

    def getSearch_ByXPATH(self):
        self.browser.find_element(*self.list_loc[5]).send_keys("Selenium")
        obiect = AutomTestPracticePage
        obiect.getSearch_Click(self)

        self.browser.maximize_window()

        elem = self.browser.find_elements(*self.list_loc[6])
        print("Elements on the page: ", len(elem))

        for i in range(len(elem)):
            elem[i].click()
            print(elem[i].text, " --- ", elem[i].get_attribute('href'))
            time.sleep(1)

        self.browser.quit()

    def getAlert_PopUp(self):
        try:
            self.browser.implicitly_wait(10)
        except:
            None

        self.browser.maximize_window()
        alert = self.browser.find_element(*self.list_loc[7]).text
        print("\n", alert)

        # we click on the alert button and print the message from it
        alert_click_button = self.browser.find_element(*self.list_loc[8])
        print("The text from the alert click box is: ", alert_click_button.text)
        alert_click_button.click()

        # we go on allert message box
        var_alert = self.browser.switch_to.alert

        # we print the message inside the alert box and click OK to close the alert box
        print("The text from the alert message box is: ", var_alert.text)
        var_alert.accept()
        msg = self.browser.find_element(*self.list_loc[9]).text
        print("The status of the alert action is : ", msg)

        time.sleep(2)

        self.browser.quit()


    def isDate_Picker(self):
        date = self.browser.find_element(*self.list_loc[10])

        # click on date picker
        if date.is_enabled():
            date.click()

        zi = self.browser.find_element(*self.list_loc[11])
        zi.click()
        luna = self.browser.find_element(*self.list_loc[12])
        an = self.browser.find_element(*self.list_loc[13])
        print('\n','The date selected is:   ', luna.text, '-', zi.text, '-', an.text)

        # today
        from datetime import date
        astazi = date.today()
        print("Today's date:", astazi)
        print("Month: ", astazi.month, "/  Day: ", astazi.day, "/  Year: ", astazi.year)

        # now
        current_date = datetime.now()
        print("Today's current date:", current_date)     # complete date and time

        # strftime
        d1 = astazi.strftime("%m/%d/%Y")
        print(d1)


        time.sleep(2)

        self.browser.quit()


    def isDate_PickerNew(self):
        date = self.browser.find_element(*self.list_loc[10])

        # click on date picker
        if date.is_enabled():
            date.click()

        self.browser.find_element(*self.list_loc[14]).click()


        time.sleep(2)

        self.browser.quit()


    def get_SignUp(self):
        self.browser.maximize_window()

        parent_frame = self.browser.find_element(*self.list_loc[15])
        self.browser.switch_to.frame(parent_frame)

        # all caterories
        vol = self.browser.find_element(*self.list_loc[16])
        print("\nCategory: ", vol.text)

        categ = self.browser.find_elements(*self.list_loc[17])
        print()
        for i in categ:
            print("Category: ", i.text)


        # name and adress
        self.browser.find_element(*self.list_loc[18]).send_keys("Gica")
        self.browser.find_element(*self.list_loc[19]).send_keys("Hagi")
        self.browser.find_element(*self.list_loc[20]).send_keys("0722000333")
        self.browser.find_element(*self.list_loc[21]).send_keys("Spain")
        self.browser.find_element(*self.list_loc[22]).send_keys("Sevilla")
        self.browser.find_element(*self.list_loc[23]).send_keys("gica@yahoo.com")

        # gender
        male = self.browser.find_element(*self.list_loc[24])
        male.click()

        # days available
        print("\nDays available: ")
        zile = self.browser.find_elements(*self.list_loc[25])
        for i in range(len(zile)-5, len(zile)-2):
            zile[i].click()
            print("     ", zile[i].text.capitalize())


        # best time to contact
        best_time = Select(self.browser.find_element(*self.list_loc[26]))
        best_time.select_by_index(2)

        # submit
        submit = self.browser.find_element(*self.list_loc[27])
        submit.click()

        time.sleep(2)

        self.browser.quit()

    def get_Table(self):
        self.browser.maximize_window()

        rows = self.browser.find_elements(*self.list_loc[28])
        col = self.browser.find_elements(*self.list_loc[29])
        print(f'\nThere are \'{len(rows)}\' rows, \'{len(col)}\' columns and a total no. of \'{len(rows) * len(col)}\' cells in our table')

        table_head = self.browser.find_elements(*self.list_loc[30])
        print()
        for i in table_head:
            print(i.text, end="                   ")
        print("\n--------------------------------------------------------------------------------------")

        first_row = self.browser.find_elements(*self.list_loc[31])
        print()
        for i in first_row:
            print(i.text, end="              ")

        second_row = self.browser.find_elements(*self.list_loc[32])
        print()
        for i in second_row:
            print(i.text, end="                  ")

        third_row = self.browser.find_elements(*self.list_loc[33])
        print()
        for i in third_row:
            print(i.text, end="                    ")

        # ro = len(rows)
        # co = len(col)

        # for i in range(2, ro + 1):
        #     for j in range(1, co + 1):
        #         cell = self.browser.find_element(*self.ALL_CELLS)
        #         print(cell.text, end="   ")
        #     print()

        self.browser.quit()


    def get_doubleClick(self):
        self.browser.maximize_window()
        d_click_one = self.browser.find_element(*self.list_loc[34])
        d_click_one.clear()
        d_click_one.send_keys("Good morning!")

        d_click_button = self.browser.find_element(*self.list_loc[35])

        actions = ActionChains(self.browser)
        actions.double_click(d_click_button).perform()

        time.sleep(3)

        self.browser.quit()

    def get_DragAndDrop(self):
        self.browser.maximize_window()
        drag = self.browser.find_element(*self.list_loc[36])
        drop = self.browser.find_element(*self.list_loc[37])

        actions = ActionChains(self.browser)
        actions.drag_and_drop(drag, drop).perform()

        time.sleep(3)

        self.browser.quit()

    def get_Slider(self):
        self.browser.maximize_window()
        slider = self.browser.find_element(*self.list_loc[38])

        print("\nInitial position of the slider: ", slider.location)

        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(slider, 150, 0).perform()

        print("Final position of the slider: ", slider.location)

        time.sleep(3)

        self.browser.quit()



