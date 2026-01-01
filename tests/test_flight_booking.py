from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # ✅ Title checkpoint
    wait.until(EC.title_contains("Swag Labs"))

    # Add product to cart
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']")
    )).click()

    # Open cart
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='shopping_cart_link']")
    )).click()

    # ✅ Wait for Checkout button (THIS FIXES YOUR ERROR)
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Fill checkout information
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Gaziza")
    driver.find_element(By.ID, "last-name").send_keys("Tanirbergen")
    driver.find_element(By.ID, "postal-code").send_keys("010000")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Confirmation
    assert "Thank you for your order!" in driver.page_source
    print("BOOKING (CHECKOUT) TEST: PASS")

except Exception as e:
    print("BOOKING TEST: FAIL")
    print(e)

finally:
    driver.quit()
