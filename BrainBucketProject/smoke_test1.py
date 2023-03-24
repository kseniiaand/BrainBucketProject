
#from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.support.select import Select
#from BrainBucketProject.webelements.browser import Browser
#from BrainBucketProject.webelements.UIElement import UIElement as Element
#from BrainBucketProject.webelements.dropdown import Dropdown
#from BrainBucketProject.webelements.checkbox import Radio_btn

#from BrainBucketProject.components.header import Header
#from BrainBucketProject.components.right_menu import Right_menu
#from BrainBucketProject.components.footer import Footer
#from BrainBucketProject.pages.login_page import LoginPage
#from BrainBucketProject.pages.registration_page import RegistrationPage
from BrainBucketProject.utils.config_reader import ConfigReader


from BrainBucketProject.components.header import Header
from BrainBucketProject.components.right_menu import Right_menu
from BrainBucketProject.components.footer import Footer
from BrainBucketProject.pages.login_page import LoginPage
from BrainBucketProject.pages.registration_page import RegistrationPage
from BrainBucketProject.utils.config_reader import ConfigReader

URL = "https://cleveronly.com/brainbucket/index.php?route=common/home"
configs = ConfigReader("config.json")

def test_registration_through_dropdown():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    driver = browser.get_driver()
    #clicking on 'My Account' dropdown

    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    #page_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'content']/h1")))
    #assert page_title.text == 'Register Account'
    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'


    registration_form.enter_first_name('Kseniia')
    registration_form.enter_last_name('Andriushchenko')
    registration_form.enter_email(configs.get_email())
    registration_form.enter_telephone('3313333333')
    registration_form.enter_first_line_address('265 Claridge Cir')
    registration_form.enter_city('Bolingbrook')
    registration_form.select_state('Illinois')
    registration_form.enter_password(configs.get_password())
    registration_form.confirm_password(configs.get_password())
    registration_form.subscribe_to_newsletter()
    registration_form.agree_to_privacy_policy()
    registration_form.submit_form()





    #part2

    account_btn = driver.find_element("xpath", "//a[@title='My Account']")
    account_btn.click()


    login_btn = driver.find_element("xpath", "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")
    login_btn.click()




    browser.shutdown()

def test_registration_from_right_menu():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    driver = browser.get_driver()

    login_page = LoginPage(browser)
    login_page.open_registration_from_menu()

    registration_form = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_form.enter_first_name('Kseniia')
    registration_form.enter_last_name('Andriushchenko')
    registration_form.enter_email('akseniia39@gmail.com')
    registration_form.enter_telephone('3313333333')
    registration_form.enter_first_line_address('265 Claridge Cir')
    registration_form.enter_city('Bolingbrook')
    registration_form.select_state('Illinois')
    registration_form.enter_password('Alpaca123456')
    registration_form.confirm_password('Alpaca123456')
    registration_form.subscribe_to_newsletter()
    registration_form.agree_to_privacy_policy()
    registration_form.submit_form()


    continue_btn = driver.find_element("xpath", "//div[@id='content']/form/div/div/input[2]")
    background_color2 = continue_btn.value_of_css_property("background-color")
    converted_background_color2 = Color.from_string(background_color2)
    assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
    continue_btn.click()

    browser.shutdown()

#Kseniia Andriushchenko 02/02/2023



def testing_right_menu():
    browser = Browser('https://cleveronly.com/brainbucket/index.php?route=account/login')
    driver = browser.get_driver()
    #clicking at order history button
    right_menu = Right_menu(browser)
    right_menu.click_order_history()

    browser.shutdown()


def testing_footer():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    driver = browser.get_driver()
    #clicking at About Us button
    footer = Footer(browser)
    footer.click_about_us_btn()

    browser.shutdown()

def logging_in():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    driver = browser.get_driver()

    login_page = LoginPage(browser)

    login_page.input_email('kseniia39@gmail.com')
    login_page.input_password('Alpaca123456')
    login_page.click_login_btn()

    browser.shutdown()


if __name__ == "__main__":
    test_registration_through_dropdown()
    test_registration_from_right_menu()
    testing_right_menu()
    testing_footer()
    logging_in()