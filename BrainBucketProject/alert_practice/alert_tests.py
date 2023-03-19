from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
import time
from BrainBucketProject.webelements.alert import Alert
from BrainBucketProject.webelements.iframe import IFrame

URL = "http://techskillacademy.net/practice/"

def test_simple_alert():
    browser = Browser(URL)
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    alert = Alert(browser)
    time.sleep(2)
    alert.accept_alert()
    time.sleep(2)

    browser.shutdown()

def test_confirmation_alert():
    browser = Browser(URL)
    confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
    confirm_btn.click()

    alert = Alert(browser)
    time.sleep(2)
    alert.dismiss_alert()

    time.sleep(2)
    msg = Element(browser, By.ID, 'msg')
    assert msg.get_text() == "You pressed CANCEL!"

    confirm_btn.click()
    alert.accept_alert()

    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()


def test_prompt_alert():
    browser = Browser(URL)
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")

    prompt_btn.click()

    alert = Alert(browser)

    time.sleep(2)
    name = "Svetlana"
    alert.enter_text(name)

    msg = "Hello {}! How are you today?".format(name)
    prompt_msg = Element(browser, By.ID, 'demo')
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL)
    iframe = IFrame(browser)
    iframe.switch_to_frame()

    time.sleep(2)
    Element(browser, By.XPATH, "//*[@class='logo__title']").wait_until_visible()

    browser.get_driver().switch_to.default_content()
    browser.shutdown()

if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_prompt_alert()
    test_iframe()














