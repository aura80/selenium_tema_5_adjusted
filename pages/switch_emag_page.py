

class emag():

    #URL
    URL2 = "https://www.emag.ro/"

    #Initializer
    def __init__(self, browser):            # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser              # instance attributes
        browser.get(self.URL2)

