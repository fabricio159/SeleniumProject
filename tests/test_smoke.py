from selenium import webdriver

def test_open_page(driver):
    # driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    assert "Swag Labs" in driver.title
    # driver.quit()