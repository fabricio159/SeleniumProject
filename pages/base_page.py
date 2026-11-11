from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import Config

Locator = tuple[str, str]

class BasePage:
    def __init__(self, driver: WebDriver, timeout: float = Config.EXPLICIT_WAIT):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path) -> "BasePage":
        self.driver.get(path)
        return self

    def findElement(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator: Locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def clickElement(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text: str):
        element = self.findElement(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator: Locator) -> str:
        return self.findElement(locator).text

    def is_visible(self, locator: Locator) -> bool:
        return any(e.is_displayed() for e in self.find_all(locator))

    @property
    def current_url(self) -> str:
        return self.driver.current_url

    @property
    def title(self) -> str:
        return self.driver.title