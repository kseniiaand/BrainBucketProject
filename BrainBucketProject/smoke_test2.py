from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="drivers/chromedriver 7")
driver.get("https://cleveronly.com/brainbucket/index.php?route=common/home")

driver.maximize_window()
#clicking on 'My Account' dropdown
account_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='My Account']")))
account_btn.click()

login_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")))
login_btn.click()

page_title = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By. XPATH, "//a[contains(text(),'Continue')]")))
assert page_title.text == 'Continue'

