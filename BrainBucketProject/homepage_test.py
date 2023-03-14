from BrainBucketProject.pages.home_page import HomePage
from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

URL = 'https://cleveronly.com/brainbucket/index.php?route=common/home'

def test_opening_all_desktops():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_all_desktops()

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "Desktops"

    browser.shutdown()

def test_opening_all_pcs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_pcs()


    picture = Element(browser, By.XPATH, "//img[@title='Samsung SyncMaster 941BW']")
    picture.wait_until_visible()

    browser.shutdown()



def test_opening_all_macs():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_mac_desktops()
    home_page.open_desktop_dropdown()

    text = Element(browser, By .XPATH, "//*[contains(text(), 'Mac (1)')][1]")
    print(text.get_text())
    assert text.get_text() == 'Mac (1)'

    browser.shutdown()





if __name__ == "__main__":
    test_opening_all_desktops()
    test_opening_all_pcs()
    test_opening_all_macs()


