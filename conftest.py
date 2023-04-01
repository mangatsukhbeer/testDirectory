from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setupDriver(request):

    chromeService = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
    chromeOptions = Options()

    options = ["--headless","--disable-gpu","--window-size=1920,1200",
               "--ignore-certificate-errors","--disable-extensions","--disable-dev-shm-usage"]
    
    for option in options:
        chromeOptions.add_argument(option)

    request.cls.driver = webdriver.Chrome(service=chromeService,options=chromeOptions)

    yield request.cls.driver
    request.cls.driver.close()
