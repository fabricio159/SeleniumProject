from selenium import webdriver
from config.config import Config
# from config.config import Config

print(Config.BROWSER)


def create_driver(browser, headless):
    browser = (browser or Config.BROWSER).lower()
    headless = Config.HEADLESS if headless is None else headless

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options = options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
    return driver



