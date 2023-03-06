from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from BrainBucketProject.webelements.actions import Actions
from selenium.webdriver.common.keys import Keys

browser = Browser('https://cleveronly.com/practice/')
driver = browser.get_driver()
# get element
double_click = Element(browser, By.XPATH, '//*[@id="card"]/p')

# create action chain object
action = Actions(browser)

# click the item
action.double_click(double_click)

background_color = Element(browser, By.ID, 'card').get_attribute('style')
assert background_color == 'background-color: rgb(255, 179, 128);'


enter_input = Element(browser, By.XPATH, '//*[@id="key_practice"]/input')
text = Element(browser, By.XPATH, '//*[@id="key_practice"]/p')
action = Actions(browser)
action.send_keys_to_element(enter_input, Keys.ENTER)
print(text.get_text())
assert text.get_text() == 'You pressed the key!'





context_menu = Element(browser, By.XPATH, '//*[@id="context_menu"]/p')
box = Element(browser, By.XPATH, '//div[@id = "context_menu"]')
action = Actions(browser)
action.right_click(box)
change_color = Element(browser, By.XPATH, "//li[contains(text(), 'Change Color')]")
change_color.click()
print(box.get_css_property('background-color'))
assert box.get_css_property('background-color') == 'rgba(204, 255, 245, 1)'




browser.shutdown()