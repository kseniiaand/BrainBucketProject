from behave import given, when, then

from BrainBucketProject.utils.config_reader import ConfigReader
from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.pages.login_page import LoginPage
from BrainBucketProject.pages.profile_page import ProfilePage
from BrainBucketProject.webelements.UIElement import UIElement as Element
from selenium.webdriver.common.by import By



URL = "https://techskillacademy.net/brainbucket/index.php?route=account/login"
configs = ConfigReader("BrainBucketProject/BDDBehave/BrainBucketTests/steps/config.ini")

@given("a web browser is at the BrainBucket login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser


@given("user is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when("user enters email and password")
def enter_email_and_password(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_user1_email())
    login_page.enter_password(configs.get_user1_password())


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()


@then("user's profile page is launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"



"""Given User is not logged in
    When Password is entered
    And User click Login button
    Then 'Warning: No match for E-Mail Address and/or Password' will be shown
    
"""



@when("password is entered")
def enter_password(context):
    login_page = context.login_page
    login_page.enter_password(configs.get_user1_password())

@when("user click Login button")
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()

@then("'Warning: No match for E-Mail Address and/or Password' will be shown")
def verify_warning(context):
    warning_title = Element(context.browser, By.XPATH, "//div[contains(text(), 'Warning: No match')]")
    assert warning_title.get_text() == 'Warning: No match for E-Mail Address and/or Password.'

"""Scenario: user can recover his password
     Given User is not logged in
     When User clicks 'Forgotten Password' button
     And enters his email
     Then Message 'An email with a confirmation link has been sent your email address.' will be dispalyed
"""


@when("user clicks 'Forgotten Password' button")
def click_forgot_pass_btn(context):
    login_page = context.login_page
    login_page.click_forgotten_pass_btn()

@when("enters his email")
def enter_email(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_user1_email())

@then("Message 'An email with a confirmation link has been sent your email address.' will be dispalyed")
def verify_email_sent(context):
    message_text = Element(context.browser, By.XPATH, "//div[contains(text(), 'An email with a confirmation')]")
    assert message_text.get_text() == 'An email with a confirmation link has been sent your email address.'




