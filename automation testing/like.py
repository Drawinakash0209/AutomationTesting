from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

print("Like test")

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


likebutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/button")))


time.sleep(5)

# Scenario 1: Logged-out user attempting to like the post
print("Scenario 1: Logged-out user attempting to like the post")
try:
    # Click the like button again
    likebutton.click()

    # Wait for a brief moment to ensure no changes occur
    time.sleep(2)

    # Get the current like count after the attempted like
    current_like_count = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/button/span/p").text

    # Verify that the like count remains unchanged
    assert current_like_count == "0", "Like count changed for logged-out user"
    print("Test pass : Logged-out user attempting to like the post")
except AssertionError as e:
    print("Scenario 2 (Logged-out user attempting to like the post): Failed -", e)

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

# Scenario 2: Logged-in user liking the post
print("Scenario 2: Logged-in user liking the post")
try:
    # Click the like button
    likebutton.click()

    # Wait for a brief moment to ensure the like count updates
    time.sleep(2)

    # Get the updated like count
    updated_like_count = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/button/span/p").text

    # Verify that the like count has increased by 1
    assert updated_like_count == "1", "Like count did not increase after clicking like button"
    print("Logged-in user liking the post: Passed")
except AssertionError as e:
    print("Failed -", e)





driver.quit()
