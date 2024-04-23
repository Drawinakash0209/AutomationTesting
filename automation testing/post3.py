from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


print("blog post feature test")
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

postbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sidenavAccordion > div.sb-sidenav-menu > div > a:nth-child(4)")))
postbutton.click()

addpostbutton = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/nav/div[1]/div/div[3]/nav/a[1]")))
addpostbutton.click()  

name = "The Rise of Artificial Intelligence in Healthcare"
slug = "the-rise-of-artificial-intelligence-in-healthcare-is-healthcare"
description = "Artificial intelligence (AI) is a rapidly evolving technology that is increasingly being used in healthcare. From improving patient outcomes to reducing costs, AI has the potential to revolutionize the way healthcare is delivered. In this post, we will explore the rise of AI in healthcare and its impact on the industry."
tags = "IT"
meta_title = "The Rise of Artificial Intelligence in Healthcare"
meta_description = "Artificial intelligence (AI) is a rapidly evolving technology that is increasingly being used in healthcare. From improving patient outcomes to reducing costs, AI has the potential to revolutionize the way healthcare is delivered. In this post, we will explore the rise of AI in healthcare and its impact on the industry."
meta_keywords = "AI, healthcare, technology, patient outcomes, costs, industry"




def correctpost(name, slug, description, tags, meta_title, meta_description, meta_keywords):
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)
    
    driver.find_element(By.NAME, "slug").clear()
    driver.find_element(By.NAME, "slug").send_keys(slug)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[4]/div/div[3]/div[2]").clear()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[4]/div/div[3]/div[2]").send_keys(description)
 
    driver.find_element(By.NAME, "tags").clear()
    driver.find_element(By.NAME, "tags").send_keys(tags)

    driver.find_element(By.NAME, "meta_title").clear()
    driver.find_element(By.NAME, "meta_title").send_keys(meta_title)

    
    driver.find_element(By.NAME, "meta_description").clear()
    driver.find_element(By.NAME, "meta_description").send_keys(meta_description)

    driver.find_element(By.NAME, "meta_keywords").clear()
    driver.find_element(By.NAME, "meta_keywords").send_keys(meta_keywords)
    time.sleep(5)

    driver.find_element(By.NAME, "terms").click()
    
    time.sleep(5)

    driver.find_element(By.NAME, "post-button").click()



print("Test case 1: Testing with Null credentials...")
correctpost("", "", "", "", "","","")
time.sleep(10)
try:
    welcome_message = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div/div[2]/div').text
    if welcome_message:
        print("Test pass: All fields are required.")
except:
    print("Test failed: Welcome message not found.")

time.sleep(10)
driver.quit()