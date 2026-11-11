from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PATH = "inventory.html"
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    INVENTORY_LIST = (By.CSS_SELECTOR, "[data-test='inventory-list']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")

    def wait_until_loaded(self):
        self.wait.until(EC.url_contains(self.PATH))
        self.findElement(self.INVENTORY_LIST)
        return self

    def is_loaded(self) -> bool:
        return self.PATH in self.current_url

    @property
    def header_title(self) -> str:
        return self.text_of(self.TITLE)

    @property
    def items(self):
        return self.find_all(self.ITEMS)
