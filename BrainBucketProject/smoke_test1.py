from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="drivers/chromedriver 7")
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

new_registrant_btn= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continue')]")))
#new_registrant_btn = driver.find_element("xpath", "//a[contains(text(),'Continue')]")
background_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registrant_btn.click()


firstname_field = driver.find_element("xpath", "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element("id", "input-firstname")
firstname_input.clear()
firstname_input.send_keys("Kseniia")


lastname_field = driver.find_element("xpath", "//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element("id", "input-lastname")
lastname_input.clear()
lastname_input.send_keys("Andriushchenko")

email_field = driver.find_element("xpath", "//fieldset/div[4]")
email_field_class = email_field.get_attribute("class")
assert"required" in email_field_class

email_input = driver.find_element("id", "input-email")
email_input.clear()
email_input.send_keys("akseniia39@gmail.com")

telephone_field = driver.find_element("xpath", "//fieldset/div[5]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class

telephone_input=driver.find_element("id", "input-telephone")
telephone_input.clear()
telephone_input.send_keys("3313333333")


fax_field = driver.find_element("xpath", "//fieldset/div[6]")
fax_field_class = fax_field.get_attribute("class")
assert "required" not in fax_field_class


fax_input = driver.find_element("id", "input-fax")
fax_input.clear()
fax_input.send_keys("3313331111")

company_field = driver.find_element("xpath", "//input[@id='input-company']")
company_field_class = company_field.get_attribute("class")
assert "required" not in company_field_class

company_input = driver.find_element ("id", "input-company")
company_input.clear()
company_input.send_keys ("AKseniia LLC")


address_field = driver.find_element("xpath", "//fieldset[@id='address']/div[2]")
address_field_class = address_field.get_attribute("class")
assert "required" in address_field_class

address_input = driver.find_element("id", "input-address-1")
address_input.clear()
address_input.send_keys("256 Claridge Cir")


address2_field = driver.find_element("xpath", "//fieldset[@id='address']/div[3]")
address2_field_class = address2_field.get_attribute("class")
assert "required" not in address2_field_class

address2_input = driver.find_element("id", "input-address-2")
address2_input.clear()
address2_input.send_keys("266 Claridge Circle")


city_field = driver.find_element("xpath", "//fieldset[@id='address']/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class

city_input = driver.find_element("id", "input-city")
city_input.clear()
city_input.send_keys("Bolingbrook")

postcode_field = driver.find_element("xpath", "//fieldset[@id='address']/div[5]")
postcode_field_class = postcode_field.get_attribute("class")
assert "required" not in postcode_field_class

postcode_input = driver.find_element("id", "input-postcode")
postcode_input.clear()
postcode_input.send_keys("60440")


password_field = driver.find_element("xpath", "//input[@id= 'input-password']")
password_input = driver.find_element("id", "input-password")
password_input.clear()
password_input.send_keys("123456")
password_field.click()

password_field = driver.find_element("xpath", "//input[@id= 'input-confirm']")
password_input = driver.find_element("id", "input-confirm")
password_input.clear()
password_input.send_keys("123456")
password_field.click()

continue_btn = driver.find_element("xpath", "//div[@id='content']/form/div/div/input[2]")
background_color2 = continue_btn.value_of_css_property("background-color")
converted_background_color2 = Color.from_string(background_color2)
assert converted_background_color2.rgb == 'rgb(34, 154, 200)'
continue_btn.click()

driver.quit()