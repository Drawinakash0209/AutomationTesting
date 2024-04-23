from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


print("survey feature test")
username = "student@gmail.com"
password = "12345678"

url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']"))
    )

userbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()

loginbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[1]")))

# Click the login link
loginbutton.click()



driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)




loginSubbutton =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.inline-flex.items-center")))
loginSubbutton.click()

userbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()

dashboardbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[2]")))
dashboardbutton.click()

surveybutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidenavAccordion > div.sb-sidenav-menu > div > a:nth-child(6)")))
surveybutton.click()

addsurveybutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/nav/div[1]/div/div[4]/nav/a[1]")))
addsurveybutton.click()


surveyName = "The Rise of Artificial Intelligence in Healthcare"
formlink = "https://docs.google.com/forms/d/e/1FAIpQLSf"
description = "Artificial intelligence (AI) is a rapidly evolving technology that is increasingly being used in healthcare. From improving patient outcomes to reducing costs, AI has the potential to revolutionize the way healthcare is delivered. In this post, we will explore the rise of AI in healthcare and its impact on the industry."


time.sleep(2)


def survey(surveyName, formlink, description):
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(surveyName)
    time.sleep(2)
    
    driver.find_element(By.NAME, "form_link").clear()
    driver.find_element(By.NAME, "form_link").send_keys(formlink)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#layoutSidenav_content > main > div > div > div.card-body > form > div:nth-child(4) > textarea").clear()
    driver.find_element(By.CSS_SELECTOR, "#layoutSidenav_content > main > div > div > div.card-body > form > div:nth-child(4) > textarea").send_keys(description)
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#layoutSidenav_content > main > div > div > div.card-body > form > div.col-md-6 > button").click()



#null values test
print("Test case 1: Testing with Null values")
survey("", "", "")
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, '//*[@id="layoutSidenav_content"]/main/div/div/div[1]').text
    if welcome_message:
        print("Test pass: Survey name, form link and description fields marked as required.")
except:
    print("Test failed: Welcome message not found.")


print("Test case 2: Testing with invalid form link")
survey(surveyName, "hey", description)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, '//*[@id="layoutSidenav_content"]/main/div/div/div[1]').text
    if welcome_message:
        print("Test pass: Invalid form link detected.")
except:
    print("Test failed: Welcome message not found.")


print("Test case 3: Testing with valid fields")
survey(surveyName, formlink, description)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, '//*[@id="layoutSidenav_content"]/main/div/div[2]').text
    if welcome_message:
        print("Test pass: Survey added successfully.")
except:
    print("Test failed: Welcome message not found.")






