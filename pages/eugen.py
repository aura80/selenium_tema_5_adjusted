import requests
from selenium.webdriver.common.by import By


class Eugen:

    URL_LINKS = "https://www.opticaeugen.ro/"

    NO_LINKS = (By.TAG_NAME, 'a')
    PAGE = (By.CSS_SELECTOR, '.layout-fullwidth.header-style-1.ls-overflow-visible')

    #Initializer
    def __init__(self, browser):         # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser           # instance attributes

    # Instances Interaction methods
    def loadPage(self):
        # we open the page https://www.opticaeugen.ro/
        self.browser.get(self.URL_LINKS)

    def get_SlidersLinks(self):
        try:
            self.browser.implicitly_wait(10)
        except:
            None

        self.browser.maximize_window()

        links = self.browser.find_elements(*self.NO_LINKS)
        self.browser.find_element(*self.PAGE)

        print(f'\n\nTile of the page:\n\n {self.browser.title} : \n\n links = {len(links)}')

        print("\n All the links on the page: \n")

        total_broken, total_ok = 0, 0
        for i in links:
            print_links = i.get_attribute('href')

            try:
                request = requests.head(print_links)
            except:
                None

            if request.status_code >= 400:
                print('   The link is broken:   ', i.text, "                              ",print_links)
                total_broken += 1
            else:
                print('   The link is ok:   ', i.text, "                              ", print_links)
                total_ok += 1

        print("----------------------------------------------------------------------------------------------")
        print("Total no. of broken links: ", total_broken)
        print("Total no. of ok links: ", total_ok)


        self.browser.quit()