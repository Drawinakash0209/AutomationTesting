from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
print("Login Feature Test")
username = "akash@gmail.com"
correct_password = "12345678"
incorrect_password = "wrongpassword"
url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

# Function to login with provided credentials
def login(email, password):
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.inline-flex.items-center").click()
    time.sleep(5)

userbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()

loginbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[1]")))

# Click the login link
loginbutton.click()

# Testing with incorrect credentials
print("test case 1:Testing with incorrect credentials...")
login(username, incorrect_password)
time.sleep(5) 

# Check if error message is displayed indicating invalid credentials
try:
    
    error_message = driver.find_element(By.XPATH, "//ul[@class='text-sm text-red-600 space-y-1 mt-2']/li").text
    if error_message:
        print("Test pass: System correctly rejects invalid credentials.")
except:
    print("Test failed: Error message not found.")

# Testing with correct credentials
print("Test Case 2: Testing with correct credentials...")
login(username, correct_password)
# Check if logged in successfully
try:
    userbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
    userbutton.click()
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[1]").text
    if welcome_message:
        print("Test pass: Logged in successfully with correct credentials.")
except:
    print("Test failed: Welcome message not found.")

# Close the browser
driver.quit()
