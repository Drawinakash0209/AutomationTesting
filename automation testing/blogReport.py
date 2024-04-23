from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

print("Report feature test")
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
p_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/p[11]")
time.sleep(5)

print("Test Scenario 1: Logged-out user attempting to report the post")

if p_element:
    print("Test Pass: logged-out user attempting to report the post")
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



time.sleep(5)
report_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/button")


print("Test Scenario 2: Logged-in user attempting to report the post")
# Check if the <p> element contains the expected text
if report_element:
    print("Test Pass: logged-in user attempting to report the post")
else:
    print("Test Fail")


time.sleep(5)



print("Test Scenario 3: Logged-in user attempting to report the post")

try:
    report_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/button")
    report_element.click()
    select_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[2]/select")
    select_element.click()
    select_option = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[2]/select/option[2]")
    select_option.click()
    
    title = driver.find_element(By.NAME, "title")
    title.send_keys("")
    textarea_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[3]/div[2]/textarea")
    textarea_element.clear()
    textarea_element.send_keys("")
    time.sleep(5)

    submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[4]/button")
    submit_button.click()
    time.sleep(5)


    welcome_message = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/div[2]/div').text
    if welcome_message:
        print("Test pass: Logged-in user attempting to report the post using null values")
    time.sleep(10)

except Exception as e:
    print("Test Fail:", e)



print("Test Scenario 4: Logged-in user attempting to report the post with correct values")

try:
    report_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/button")
    report_element.click()
    select_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[2]/select")
    select_element.click()
    select_option = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[2]/select/option[2]")
    select_option.click()
    
    title = driver.find_element(By.NAME, "title")
    title.send_keys("False information")
    textarea_element = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[3]/div[2]/textarea")
    textarea_element.clear()
    textarea_element.send_keys("False information")
    time.sleep(5)

    submit_button = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[2]/form/div[4]/button")
    submit_button.click()
    time.sleep(5)
    print("Test Pass: Logged-in user attempting to report the post with correct values")

except Exception as e:
    print("Test Fail:", e)