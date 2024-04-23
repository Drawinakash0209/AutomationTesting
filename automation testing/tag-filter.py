from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

username = "student@gmail.com"
password = "12345678"

url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']"))
    )


print("Test case: blog tags are working")
time.sleep(3)
tagbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/div/div/div[1]/div/div/div[1]/div[9]/div/div/a")))
tagbutton.click()
time.sleep(10)
try:
    time.sleep(5)
    if driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/div/div[1]/div[9]/div/div").is_displayed():
        print("test pass: tags are displayed")
except:
    print("test fail: tags are not displayed")
