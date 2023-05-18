from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException

class Browser:
    def __init__(self, url, browser_name="", time_wait = 10, username ="", accesskey =""):
        try:
            if browser_name.lower() == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument("--width=412")
                options.add_argument("--height=915")

                firefox_profile = webdriver.FirefoxProfile()
                firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
                firefox_profile.set_preference("browser.urlbar.showPopup", True)

                self.driver = webdriver.Firefox(firefox_profile=firefox_profile, executable_path='drivers/geckodriver')
                self.driver.maximize_window()
            elif browser_name.lower() == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                options.add_argument("--window-size=412,915")
                options.add_argument("--incognito")
                options.add_argument("--disable-extensions")
                options.add_argument("--disable-popup-blocking")
                options.add_experimental_option("excludeSwitches", ['enable-automation'])
                self.driver = webdriver.Chrome(executable_path='drivers/chromedriver 7', options = options)
            elif browser_name.lower() == "remote":
                BROWSERSTACK_URL = 'https://'+username+':'+ accesskey+'@hub-cloud.browserstack.com/wd/hub'

                desired_cap = {

                    'os': 'Windows',
                    'os_version': '10',
                    'browser': 'Chrome',
                    'browser_version': '80',
                    'name': "kseniiaandriushc 's First Test"

                }
                self.driver = webdriver.Remote(command_executor=BROWSERSTACK_URL, desired_capabilities=desired_cap)

        except WebDriverException:
            print("Error: executable path to driver is incorrect")
            quit()

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.implicitly_wait(time_wait)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()