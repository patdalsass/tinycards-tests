import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#python -m pytest tinycards_oop.py
class TestLogin():

    @pytest.fixture
    def driver(self, request):
        # get the path of ChromeDriver, create a Chrome driver instance
        chrome_driver_path = "/Users/patdalsass/Downloads/chromedriver"
        driver_ = webdriver.Chrome(chrome_driver_path)

        #driver_ = webdriver.Firefox()
        #test again since you're now using Firefox ESR not Geckodriver

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self, driver):
        # navigate to the application home page
        driver.get("http://tiny.cards")
        driver.implicitly_wait(30)
        driver.maximize_window()

        #find and click login button
        driver.find_element(By.CSS_SELECTOR, "button._1HImu").click()

        #find and send username/password
        driver.find_element(By.CSS_SELECTOR, "input._2a16Y._3jLx2").send_keys("Harold911125")
        driver.find_element(By.CSS_SELECTOR, "input._3FjlE._3jLx2").send_keys("duolingo")


        #click Let's Go!
        driver.find_element(By.CSS_SELECTOR, "button._128yG.VJ841").click()

        #If "Your Favorites" is displayed on the page, the test passes - note there are 3 divs on the page with this same class. Test will work, but ask about a better approach- xpath?
        assert driver.find_element(By.CLASS_NAME, "_3uLNI").is_displayed()
        time.sleep(3)
