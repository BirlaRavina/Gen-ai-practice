# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# print('working...')
# username = driver.find_element(By.CSS_SELECTOR, 'input.oxd-input.oxd-input--active[name="username"]')
# password = driver.find_element(By.CSS_SELECTOR, 'input.oxd-input[name= "password"]')
# login_btn = driver.find_element(By.CSS_SELECTOR, 'button.orangehrm-login-button')
# print(login_btn)
# username.send_keys('Admin')
# password.send_keys('admin123')
# login_btn.click()
# assert 'Dashboard' in driver.title
# # time.sleep(5)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

print('working...')
# username = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.oxd-input[name="username"]'))
# )
username = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@placeholder = "Username"]'))
)

password = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.oxd-input[name="password"]'))
)

login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.orangehrm-login-button'))
)


username.send_keys('Admin')
password.send_keys('admin123')
login_btn.click()
print(driver.current_url)
try:
    # Wait until the Dashboard title is loaded
    WebDriverWait(driver, 10).until(
        EC.title_contains('Dashboard')
    )


    print(driver.current_url)
    print('hee')
    admin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//li/a//span[text()="Admin"]/parent::a'))
    )
    admin.click()
    time.sleep(5)
except Exception as e:
    print(e)

# time.sleep(5)
assert "OrangeHRM" in driver.title

print("Navigated to Admin module")

driver.quit()

# //input[@type='checkbox' and @value='5']











# time.sleep(5)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Start Chrome browser
# driver = webdriver.Chrome()

# # Navigate to the login page
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# # Locate the username, password fields, and the login button
# username = driver.find_element(By.NAME, 'username')
# password = driver.find_element(By.NAME, 'password')
# login_btn = driver.find_element(By.NAME, 'orangehrm-login-button')

# # Print the login button (optional for debugging)
# print("this is login btn",login_btn)

# # Input credentials and click the login button
# username.send_keys('Admin')
# password.send_keys('admin123')
# login_btn.click()

# # Assert that the login was successful by checking the page title
# assert 'Dashboard' in driver.title

# # Wait for a few seconds to see the result
# time.sleep(5)

# # Close the browser
# driver.quit()
