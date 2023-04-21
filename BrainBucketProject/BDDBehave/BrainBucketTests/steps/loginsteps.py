from behave import given, when, then

from BrainBucketProject.utils.config_reader import ConfigReader
from BrainBucketProject.webelements.browser import Browser
from BrainBucketProject.pages.login_page import LoginPage
from BrainBucketProject.pages.profile_page import ProfilePage


URL = "https://techskillacademy.net/brainbucket/index.php?route=account/login"
configs = ConfigReader("BrainBucketTests/BDDBehave/logintests/steps/config.ini")

@given("user launch login page")
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

@given("user launch login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser

