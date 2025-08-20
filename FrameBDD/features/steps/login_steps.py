from behave import given, when, then
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I open the login page")
def step_open_login_page(context):
    context.page = LoginPage(context.driver)
    context.page.open()

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.page.enter_username(username)
    context.page.enter_password(password)
    context.page.click_login()

@then('I should get new page with url "{url}"')
def step_verify_URL(context, url):
    WebDriverWait(context.driver, 10).until(EC.url_to_be(url))
    current_url = context.page.get_current_url()
    assert current_url == url, f"Expected URL to be {url}, but got {current_url}"

# @then('I should see message "{expected}"')
# def step_verify_message(context, expected):
#     assert expected in context.page.get_flash_message()