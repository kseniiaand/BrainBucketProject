from behave import *
from BrainBucketProject.pages.login_page import LoginPage

"""
    Given the user is not logged in
    When the user enters their "<credential>"
    And the user clicks Login button
    Then the warning message "<warning>" is displayed
    """


@given('the user is not logged in')
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when('the user enters their "{credential}"')
def type_credential(context, credential):
    login_page = context.login_page
    configs = context.configs
    context.login_page = login_page

    if credential == "email only ":
        login_page.input_email(credential)
    elif credential == "password only":
        login_page.input_password(credential)


@when('the user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()

@then('the warning message "<warning>" is displayed')
def verify_warning_is_displayed(context, warning):
    login_page = LoginPage(context.browser)
    assert login_page.get_warning_title() == 'No match for E-Mail Address and/or Password'
    context.login_page = login_page

