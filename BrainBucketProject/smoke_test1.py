from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.select import Select
from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.webelements.UIElement import UIElement as Element
from BrainBucketProject.webelements.dropdown import Dropdown


browser = Browser("https://cleveronly.com/brainbucket/index.php?route=common/home")
driver = browser.get_driver()
#clicking on 'My Account' dropdown

account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
account_btn.click()


register_btn = Element(browser, By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li/a")
register_btn.click()


page_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'content']/h1")))
assert page_title.text == 'Register Account'




firstname_field = Element(browser, By.XPATH, "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute('class')
assert "required" in firstname_field_class
firstname_input = Element(browser, By.ID, "input-firstname")
firstname_input.enter_text("Kseniia")



lastname_field = Element(browser, By.XPATH, "//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute('class')
assert "required" in lastname_field_class
lastname_input = Element(browser, By.ID, "input-lastname")
lastname_input.enter_text("Andriushchenko")



email_field = Element(browser,By.XPATH, "//fieldset/div[4]")
email_field_class = email_field.get_attribute('class')
assert 'required' in email_field_class
email_input = Element(browser, By.ID,  "input-email")
email_input.enter_text("akseniia39@gmail.com")



telephone_field = Element(browser, By.XPATH, "//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute('class')
assert 'required' in telephone_field_class
telephone_input = Element(browser, By.ID, "input-telephone")
telephone_input.enter_text('3313333333')


fax_field = Element(browser, By.XPATH, "//fieldset/div[6]")
fax_field_class = fax_field.get_attribute('class')
assert 'required' not in fax_field_class
fax_input = Element(browser, By.ID, "input-fax")
fax_input.enter_text("3313331111")


company_field = Element(browser, By.XPATH, "//input[@id='input-company']")
company_field_class = company_field.get_attribute('class')
assert 'required' not in company_field_class
company_input = Element(browser, By.ID, "input-company")
company_input.enter_text("AKseniia LLC")


address_field = Element(browser, By.XPATH, "//fieldset[@id='address']/div[2]")
address_field_class = address_field.get_attribute('class')
assert 'required' in address_field_class
address_input = Element(browser, By.ID, "input-address-1")
address_input.enter_text("270 Lily Cash Ln")


address2_field = Element(browser, By.XPATH, "//fieldset[@id='address']/div[3]")
address2_field_class = address2_field.get_attribute('class')
assert 'required' not in address2_field_class
address2_input = Element(browser, By.ID, "input-address-2")
address2_input.enter_text("266 Claridge Cir")


city_field = Element(browser, By.XPATH, "//fieldset[@id='address']/div[4]")
city_field_class = city_field.get_attribute('class')
assert 'required' in city_field_class
city_input = Element(browser, By.ID, "input-city")
city_input.enter_text("Bolingbrook")


postcode_field = Element(browser, By.XPATH, "//fieldset[@id='address']/div[5]")
postcode_field_class = postcode_field.get_attribute('class')
assert 'required' not in postcode_field_class
postcode_input = Element(browser, By.ID, "input-postcode")
postcode_input.enter_text("60440")


password_field = Element(browser, By.XPATH, "//input[@id= 'input-password']")
password_input = Element(browser, By.ID, "input-password")
password_input.enter_text("123456")
password_input.click()


pass_confirm_field = Element(browser, By.XPATH, "//input[@id= 'input-confirm']")
pass_confirm_input = Element(browser, By.ID, "input-confirm")
pass_confirm_input.enter_text("123456")
pass_confirm_input.click()



#select country

Dropdown(browser, By.ID, 'input-country').select_by_value('223')

#select state


Dropdown(browser, By.ID, 'input-zone').select_by_text('Illinois')

subscribe_btn = driver.find_element("xpath", "//div[@id='content']/form/fieldset[4]/div/div/label[2]")
if not subscribe_btn.is_selected():
    subscribe_btn.click()




policy_btn = driver.find_element("xpath", "//div[@id='content']/form/div/div/input")
if not policy_btn.is_selected():
    policy_btn.click()

continue_btn = driver.find_element("xpath", "//div[@id='content']/form/div/div/input[2]")
background_color2 = continue_btn.value_of_css_property("background-color")
converted_background_color2 = Color.from_string(background_color2)
assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
continue_btn.click()



#part2

account_btn = driver.find_element("xpath", "//a[@title='My Account']")
account_btn.click()


login_btn = driver.find_element("xpath", "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")
login_btn.click()




browser.shutdown()