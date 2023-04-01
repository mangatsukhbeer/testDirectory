import pytest
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

@pytest.mark.usefixtures("setupDriver")
class TestOne:

    def waitClickFunction(driver: webdriver, xpath: str,ac:ActionChains):
        wait = WebDriverWait(driver, timeout=30,
                            poll_frequency=0.5,
                            ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

        resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        if resultingElement == '':
            return False
        else:
            ac.click(resultingElement).perform()
            return True
        return False

    def waitFunction(driver: webdriver, xpath: str,ac:ActionChains):
        wait = WebDriverWait(driver, timeout=30,
                            poll_frequency=0.5,
                            ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

        resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        if resultingElement == '':
            return False
        else:
            return True
        return False

    def waitSendKeys(driver: webdriver, xpath: str,keys:str,ac:ActionChains):
        wait = WebDriverWait(driver, timeout=30,
                            poll_frequency=0.5,
                            ignored_exceptions=[ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException])

        resultingElement = wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        if resultingElement == '':
            return False
        else:
            ac.send_keys_to_element(resultingElement,keys).perform()
            return True
        return False

    def test_loadWebsite(self,website,title):

        self.driver.get(website)
        assert self.driver.title == title
        print(self.driver.title)
    

testCase = TestOne()
testCase.test_loadWebsite('https://www.google.ca','Google')
