from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element("xpath", "//img[@title='Brainbucket']")

new_registrant_btn = driver.find_element("xpath", "//a[contains(text(),'Continue'))")
background_color = new_registrant_btn.value_of_css_property("background_color")
converted_background_color=Color.from_string("background-color")
assert converted_background_color.rgb == 'rgb(34,154,200)'
new_registrant_btn.click()


firstname_field = driver.find_element("xpath", "//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element("id", "input-firstname")
firstname_input.clear()
firstname_input.send_keys("Lana")



# 11/5/2022
# Kseniia Andriushchenko


password_field = driver.find_element("id", "input-password")
password_field.clear()
password_field.send_keys("123456")

login_btn = driver.find_element("xpath", "//input[@class='btn btn-primary']")
login_btn.click()

lastname_field = driver.find_element("xpath", "//fieldset/div[3]")
lastname_field_class = lastname_field.get_attribute("class")
assert"required" in lastname_field_class

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
assert "required" in fax_field_class

fax_input = driver.find_element("id", "input-fax")
fax_input.clear()
fax_input.send_keys("3313331111")


address_field = driver.find_element("xpath", "//fieldset/div[2]")
address_field_class = address_field.get_attribute("class")
assert "required" in address_field_class

address_input = driver.find_element("id", "input-address-1")
address_input.clear()
address_input.send_keys("256 Claridge Cir")

city_field = driver.find_element("xpath", "//fieldset/div[4]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class

city_input = driver.find_element("id", "input-city")
city_input.clear()
city_input.send_keys("Bolingbrook")

password_field = driver.find_element("xpath", "//fieldset/div[1]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class

password_input = driver.find_element("id", "input-password")
password_input.clear()
password_input.send_keys("123456")

passwordcnfrm_field = driver.find_element("xpath", "//fieldset/div[2]")
passwordcnfrm_field_class = passwordcnfrm_field.get_attribute("class")
assert "required" in passwordcnfrm_field_class

passwordcnfrm_input = driver.find_element("id", "input-confirm")
passwordcnfrm_input.clear()
password_input.send.keys("123456")

background_color =new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34,154,200)'

