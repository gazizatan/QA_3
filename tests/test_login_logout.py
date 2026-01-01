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

    # Verify login
    wait.until(EC.url_contains("inventory"))

    # Open burger menu
    wait.until(EC.element_to_be_clickable(
        (By.ID, "react-burger-menu-btn")
    )).click()

    # Logout (wait until visible)
    wait.until(EC.element_to_be_clickable(
        (By.ID, "logout_sidebar_link")
    )).click()

    # Verify logout
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    print("LOGIN & LOGOUT TEST: PASS")

except Exception as e:
    print("LOGIN & LOGOUT TEST: FAIL")
    print(e)

finally:
    driver.quit()
