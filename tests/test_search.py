from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")

    # Login first
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    # "Search" by checking product name
    product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")

    assert product.is_displayed()
    print("SEARCH TEST: PASS")

except Exception as e:
    print("SEARCH TEST: FAIL", e)

finally:
    driver.quit()
