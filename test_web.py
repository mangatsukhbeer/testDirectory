import unittest
import pytest
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class WebTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromeService = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        chromeOptions = Options()

        options = ["--headless","--disable-gpu","--window-size=1920,1200",
                "--ignore-certificate-errors","--disable-extensions","--disable-dev-shm-usage"]
        
        for option in options:
            chromeOptions.add_argument(option)

        cls.driver = webdriver.Chrome(service=chromeService,options=chromeOptions)
        cls.ac = ActionChains(driver=cls.driver)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    
    def waitClickFunction(self, xpath: str):
        wait = WebDriverWait(self.driver, timeout=30,
                            poll_frequency=0.5,
                            ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

        resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        if resultingElement == '':
            return False
        else:
            self.ac.click(resultingElement).perform()
            return True
        return False

    def waitSendKeys(self,xpath: str,keys:str):
        wait = WebDriverWait(self.driver, timeout=30,
                            poll_frequency=0.5,
                            ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

        resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        if resultingElement == '':
            return False
        else:
            self.ac.send_keys_to_element(resultingElement,keys).perform()
            return True
        return False

    def screenshot(self,name):
        try:
            self.driver.save_screenshot(f'{name}.png')
            return True
        except:
            return False
        
    
    def test_01_websiteLoad(self,url="https://www.google.ca",title="Google"):

        self.driver.get(url)
        websiteTitle = self.driver.title
        print(websiteTitle)
        assert websiteTitle == title
    
    def test_02_searchInputClick(self,xpath='//input[@aria-label="Search"]'):
        assert self.waitClickFunction(xpath=xpath)
    
    def test_03_sendSearchKeys(self,xpath='//input[@aria-label="Search"]',keys="Sukhbeer Mangat"):
        assert self.waitSendKeys(xpath,keys)
    
    def test_04_searchButtonClick(self,xpath='//input[@aria-label=Google Search"]'):
        assert self.waitClickFunction(xpath=xpath)
    
    def test_05_takeScreenshot(self,name="testShot"):
        assert self.screenshot(name)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Teardown done")

if __name__ == '__main__':
    logfile = "log.txt"
    with open(logfile,"w") as file:
        runner = unittest.TextTestRunner(file)
        unittest.main(testRunner=runner)

# @pytest.fixture()
# def test_setup():
#     global driver
#     chromeService = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
#     chromeOptions = Options()

#     options = ["--headless","--disable-gpu","--window-size=1920,1200",
#             "--ignore-certificate-errors","--disable-extensions","--disable-dev-shm-usage"]
    
#     for option in options:
#         chromeOptions.add_argument(option)

#     driver = webdriver.Chrome(service=chromeService,options=chromeOptions)
#     driver.implicitly_wait(30)
#     driver.maximize_window()

#     yield
#     driver.close()
#     driver.quit()



# def waitClickFunction(driver: webdriver, xpath: str,ac:ActionChains):
#     wait = WebDriverWait(driver, timeout=30,
#                         poll_frequency=0.5,
#                         ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

#     resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
#     if resultingElement == '':
#         return False
#     else:
#         ac.click(resultingElement).perform()
#         return True
#     return False

# def waitFunction(driver: webdriver, xpath: str,ac:ActionChains):
#     wait = WebDriverWait(driver, timeout=30,
#                         poll_frequency=0.5,
#                         ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

#     resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
#     if resultingElement == '':
#         return False
#     else:
#         return True
#     return False

# def waitSendKeys(driver: webdriver, xpath: str,keys:str,ac:ActionChains):
#     wait = WebDriverWait(driver, timeout=30,
#                         poll_frequency=0.5,
#                         ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

#     resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
#     if resultingElement == '':
#         return False
#     else:
#         ac.send_keys_to_element(resultingElement,keys).perform()
#         return True
#     return False

# def test_loadWebsite(test_setup,website="https://www.google.ca",title="Google"):

#     driver.get(website)
#     driver.save_screenshot('test.png')
#     assert driver.title == title
#     print(driver.title)


