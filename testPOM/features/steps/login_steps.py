from behave import given, when, then
from pages.login_page import LoginPage

@given("I open the login page")
def step_open_login_page(context):
    context.page = LoginPage(context.driver)
    context.page.open()

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.page.enter_username(username)
    context.page.enter_password(password)
    context.page.click_login()

@then('I should see message "{expected}"')
def step_verify_message(context, expected):
    assert expected in context.page.get_flash_message()
