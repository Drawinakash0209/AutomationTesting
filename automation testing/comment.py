from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


print("Comment Feature Test")
username = "student@gmail.com"
password = "12345678"

url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']"))
    )

postbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[1]/div/div/div[1]/div[1]/a")))
postbutton.click()



# Find the <p> element
p_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/p[10]")
time.sleep(5)

print("Test Scenario 1: Logged-out user attempting to comment the post")
# Check if the <p> element contains the expected text
if p_element:
    print("Test Pass: logged-out user attempting to comment the post")
else:
    print("Test Fail")


driver.back()


userbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()
loginbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[1]")))
loginbutton.click()
driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
loginSubbutton =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inline-flex.items-center")))
loginSubbutton.click()
time.sleep(3)
postbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[1]/div/div/div[1]/div[1]/a")))
postbutton.click()
likebutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/button")))




comment_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[1]/div[1]/div/h2")
time.sleep(5)

print("Test Scenario 2: displaying comment option to logged-in user")
# Check if the <p> element contains the expected text
if comment_element:
    print("Test Pass: logged-in user attempting to comment the post")
else:
    print("Test Fail")


time.sleep(5)


print("Test Scenario 3: Logged-in user attempting to comment the post")
try:
    # Find the textarea element
    textarea_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[1]/div[1]/div/div[1]/textarea")
    textarea_element.clear()
    textarea_element.send_keys("Great post!")
    commentsubmit =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[1]/div[1]/div/div[2]/button")))  
    commentsubmit.click()
    print("Test Pass: logged-in user attempting to comment the post successfully")
except Exception as e:
    print("Test Fail:", e)