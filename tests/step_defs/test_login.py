from pytest_bdd import given, parsers, scenarios, then, when

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Collects every scenario in the feature file as a pytest test
scenarios("../features/login.feature")


@given("I am on the login page", target_fixture="login_page")
def login_page(driver) -> LoginPage:
    return LoginPage(driver).load()


@when(parsers.parse('I log in as "{username}" with password "{password}"'))
def log_in(login_page: LoginPage, username: str, password: str):
    login_page.submit_credentials(username, password)


@then("I should see the products page")
def on_products_page(driver):
    assert InventoryPage(driver).wait_until_loaded().is_loaded()


@then(parsers.parse('the page header should be "{title}"'))
def header_is(driver, title: str):
    assert InventoryPage(driver).header_title == title


@then(parsers.parse('I should see the error "{error}"'))
def error_shown(login_page: LoginPage, error: str):
    assert login_page.error_message == error
