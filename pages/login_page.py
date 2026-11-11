from selenium.webdriver.common.by import By
from config.config import Config

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self) -> "LoginPage":
        self.open(Config.BASE_URL)
        return self

    def submit_credentials(self, username: str, password: str) -> None:
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.clickElement(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> InventoryPage:
        self.submit_credentials(username, password)
        return InventoryPage(self.driver).wait_until_loaded()

    @property
    def error_message(self) -> str:
        return self.text_of(self.ERROR)
