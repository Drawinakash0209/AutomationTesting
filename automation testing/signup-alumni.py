from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

print("Alumni Signup Feature Test")

graduated_year = "2018"
nic = "200000011V"
alumni_degree = "BSc in Computer Science"
name = "Harrish"
email = "harrish@gmail.com"
password = "12345678"
password_confirmation = "12345678"


url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

# Function to login with provided credentials
def signup(graduated_year, nic, alumni_degree, name, email, password, password_confirmation):
    driver.find_element(By.NAME, "graduated_year").clear()
    driver.find_element(By.NAME, "graduated_year").send_keys(graduated_year)

    driver.find_element(By.NAME, "nic").clear()
    driver.find_element(By.NAME, "nic").send_keys(nic)

    driver.find_element(By.NAME, "alumni_degree").clear()
    driver.find_element(By.NAME, "alumni_degree").send_keys(alumni_degree)

    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
  
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "password_confirmation").clear()
    driver.find_element(By.NAME, "password_confirmation").send_keys(password_confirmation)

    driver.find_element(By.CSS_SELECTOR, "body > div.min-h-screen.flex.flex-col.sm\:justify-center.items-center.pt-6.sm\:pt-0.bg-gray-100 > div.w-full.sm\:max-w-md.mt-6.px-6.py-4.bg-white.shadow-md.overflow-hidden.sm\:rounded-lg > form > div.flex.items-center.justify-end.mt-4 > button").click()


def signup_with_error(graduated_year, nic, alumni_degree, name, email, password, password_confirmation):
    driver.find_element(By.NAME, "graduated_year").clear()
    driver.find_element(By.NAME, "graduated_year").send_keys(graduated_year)

    driver.find_element(By.NAME, "nic").clear()
    driver.find_element(By.NAME, "nic").send_keys(nic)

    driver.find_element(By.NAME, "alumni_degree").clear()
    driver.find_element(By.NAME, "alumni_degree").send_keys(alumni_degree)

    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
  
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "password_confirmation").clear()
    driver.find_element(By.NAME, "password_confirmation").send_keys(password_confirmation)

    driver.find_element(By.CSS_SELECTOR, "body > div.min-h-screen.flex.flex-col.sm\:justify-center.items-center.pt-6.sm\:pt-0.bg-gray-100 > div.w-full.sm\:max-w-md.mt-6.px-6.py-4.bg-white.shadow-md.overflow-hidden.sm\:rounded-lg > form > div.flex.items-center.justify-end.mt-4 > button").click()





userbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()


signupbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[2]")))
signupbutton.click()

userType = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/select")))
userType.click()

alumni = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/select/option[2]")))
alumni.click()
time.sleep(3)

# Testing with null
print("Test case 1:Testing with null Email")
signup(graduated_year, nic, alumni_degree, name, "", password, password_confirmation)
time.sleep(5)
try:
    email_input = driver.find_element(By.NAME, "email")
    if "required" in email_input.get_attribute("outerHTML"):
        print("Test pass: email field is marked as required.")
except:
    print("Test failed: email field not marked as required.")


# Testing with null
print("Test case 2:Testing with same NIC")
signup(graduated_year, "200000000V", alumni_degree, name, email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[8]/ul/li").text
    if welcome_message:
        print("Test pass: Cannot register with same NIC.")
except:
    print("Test failed: Welcome message not found")



# Testing with incorrect credentials - Batch
print("Test case 3:Testing with null Password")
signup(graduated_year, nic, alumni_degree, name, email, "", password_confirmation)
time.sleep(5)
try:
    password_input = driver.find_element(By.NAME, "password")
    if "required" in password_input.get_attribute("outerHTML"):
        print("Test pass: password field is marked as required.")
except:
    print("Test failed: password field not marked as required.")








# Testing with incorrect credentials - different passwords
print("Test case 4:Testing with different passwords ...")
signup(graduated_year, nic, alumni_degree, name, email, "123456789", password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[15]/ul").text
    if welcome_message:
        print("Test pass: Cannot register with two different passwords.")
except:
    print("Test failed: Welcome message not found")




# Testing with correct credentials
print("Test case 5:Testing with correct credentials...")
signup(graduated_year, nic, alumni_degree, name, email, "12345678", password_confirmation)
time.sleep(5)  # Wait for 5 seconds

# Check if logged in successfully
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div").text
    if welcome_message:
        print("Test pass: Signed-in successfully with correct credentials.")
except:
    print("Test failed: Welcome message not found.")

# Close the browser
driver.quit()
