# selenium_tema_5_adjusted
basic framework using python, selenium
# Setup Instructions
Python Setup
Download the latest Python version from Python.org.
Download a Python editor/IDE of your choice. PyCharm in this case.
# Git Setup
Create an account on Github.com
Download GitHub for desktop
# New Project Setup
 * Create a new repository in GitHub :
   * Click New
   * Complete Repository name
   * Add a description (Optional)
   * Check Add a README file (complete this with details about project setup and how to run the tests) 
   * Add  python .gitignore file
   * Choose MIT Licence

Open in Github for desktop and clone on your machine: 
Click Code -> Open with Github for desktop
Click clone (The new repository appear on your machine)
Keep you project up to date on github : commit and push

Open the new repository(project) with the python editor (Pycharm)

# Install dependencies
pip install pipenv   -  to facilitate the installation of other libraries
pipenv install pytest
pipenv install selenium
pipenv install webdriver_manager
pipenv install pytest-html   -   for the .html report
run pipenv install pytest-xdist  -  for run in parallel

# Description of the project

        Hello! My name is Aura and I created this project in order to exercise my automation testing skills using pytest and Selenium 
    frameworks. I created a new repository named 'selenium_tema_5_adjusted' using the github and I cloned it locally. After that I 
    opened the new project on my Pycharm environment and I created two packages named 'pages' and 'tests'. 

        In the package 'pages' I added six python files which contains the classes defined by me to test the content of all the URL's 
    chosen individually. To make my work cleaner and easier, because they were too many, I wrote all the locators from the class 
    AutomTestPracticePage in the 'locators.py' file and in the 'Locators' class using the principle of inheritance. 'Locators' class 
    from 'locators.py' file became the parent class and the class 'AutomTestPracticePage' from the 'automation_page.py' file became 
    the child class. 

        The pages tested by me are:
            https://testautomationpractice.blogspot.com/
            https://demo.nopcommerce.com/
            https://www.opticaeugen.ro/
            https://www.snapdeal.com/products/mens-tshirts-polos?sort=plrty&utm_source=earth_semnonbrand&utm_medium=disp&utm_content=TShirts&utm_campaign=menapparel&utm_term=24101418888&gclid=Cj0KCQjwyMiTBhDKARIsAAJ-9VsHirTiaacBcFZQa5sTkth3Nzy0hxe-ZAXU9uBlpTg4nuppyLRMObAaAm-eEALw_wc
            https://www.amazon.com/
            https://www.emag.ro/

        The classes created by me are:
            AutomTestPracticePage, DemoNopCommerce, Eugen, Locators, DemoSlider, amazon, emag.

        The two parent classes, 'emag' and 'Locators', used by me were imported in the child classes files accordingly.
        All my classes contain the URL of the page to be tested, the appropriate locators, the constructer which sets the initial 
    state of an object and which is called every time a new object is created and the interaction methods. My locators were chosen 
    by CSS_SELECTOR, XPATH, LINK_TEXT, TAG_NAME, NAME or by ID. Every time I loaded the page first, using the get() method, before 
    implementing other methods:     
                                    def loadPage(self):
                                        self.browser.get(self.URL)

        The imports made by me at the beginiing of the files are: time, datetime, By (for locators), ActionChains (for mouse actions), 
    Select (for selections ex. dropdown), requests (for links), EC (expected conditions, for waits), WebDriverWait (for explicit wait), 
    NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException (for explicit wait), emag and Locators (inheritance).

        In the package 'tests' I added the files 'conftest.py' and 'test_automation_page.py'.
        In the 'conftest.py' file I have a fixture function named 'browser'. That function is marked as fixture by: @pytest.fixture .
    That function will run before each test function to which it is applied and will supply the input to the tests. While a test is 
    getting executed, pytest will see the fixture name as input parameter, then executes the fixture function and the returned value is 
    stored to the input parameter, which can be used later by the tests. 
        I defined the fixture function in the 'conftest.py' file in order to be available to all my test files. The tests will look for 
    the fixture in their own files, but because it will not be found there it will be checked in the 'conftest.py' file. There it will 
    be found, the fixture method will be invoked and the result will be returned as the input argument of the test.
        Inside of the function I initialized the Chrome driver instance and opened the Chrome tab using the Service and the ChromeDriverManager 
    imports for the line below:
                                   driver = selenium.webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        The function is a generator function because it uses the keyword 'yield' inside. Yield it is used when we want to iterate over 
    a sequence but we don't want to keep all the values obtained in the memory. We use 'yield' instead of 'return' because return sends 
    just a specific value back to it's caller and yield can send back a sequence of values back to it's caller. yield driver will 
    return the webdriver instance.
    In the end of the file the driver is closed using driver.quit().
        
        The 'test_automation_page.py' file contains all the main five classes imported at the beginning. Below are the twenty-one test 
    methods which begin with 'test' in their name and have 'browser' as a parameter. In every method I firstly made an object 
    corresponding to the adequate class and then I used it to call the load page function and the adequate function from the page files. 
        All the tests were generated in the order of their implementation in the 'test_automation_page.py' file.


        Firstly I installed the pipenv library to facilitate the installation of other libraries. The first commands given by me 
    using the terminal console were:
            pip install pipenv
            pipenv install pytest
            pipenv install selenium
            pipenv install webdriver_manager
            pipenv install pytest-html
            run pipenv install pytest-xdist         # to run tests in paralel

        When all the project was implemented, I run it entirelly, in terminal console, using the command:
                                    pipenv run python -m pytest
    or:
                                    pipenv run python -m pytest -s -v
    or to run 3 tests in paralel:
                                    run pipenv run python -m pytest -n 3
    or to run an entire file:
                                    pipenv run python -m pytest tests/test_automation_page.py
    or for one test only, by example:
                                    pipenv run python -m pytest tests/test_automation_page.py::test_get_Links
        
        When all my tests were passed I generated a .html report using:
                                    pipenv run python -m pytest --html=report.html

        The report.html file can be opened from Pycharm Project menu by right clicking it then press Open In, then Browser and then 
    you may choose which browser you want to open the report with.   
        
        To download my project on your machine you have to follow the link https://github.com/aura80/selenium_tema_5_adjusted then 
    click Code and Open with GitHub Desktop --> Clone repository --> URL --> Choose the local path you want to save it locally --> 
    hit Clone --> open it from Pycharm

         Another method is to find the folder where you want to save the project locally and open there a terminal window. In the 
    terminal write the line below and press enter:
                                    git clone https://github.com/aura80/selenium_tema_5_adjusted.git
    After that you can open it from Pycharm.
 

