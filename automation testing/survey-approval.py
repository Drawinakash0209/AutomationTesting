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

print("survey approval feature test")


email = "admin1@admin.com"
password = "12345678"



url = "https://group-6.laravelsrilanka.com/admin/login"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

# Function to login with provided credentials
def login(email, password):

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
  
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.CSS_SELECTOR, "body > div.min-h-screen.flex.flex-col.sm\:justify-center.items-center.pt-6.sm\:pt-0.bg-gray-100 > div.w-full.sm\:max-w-md.mt-6.px-6.py-4.bg-white.shadow-md.overflow-hidden.sm\:rounded-lg > form > div.flex.items-center.justify-end.mt-4 > button").click()
    time.sleep(3)


login(email, password)


# Function to approve a blog
def approve_survey():
    driver.find_element(By.CSS_SELECTOR, "#sidenavAccordion > div.sb-sidenav-menu > div > a:nth-child(12)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/nav/div[1]/div/div[7]/nav/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/table/tbody/tr[1]/td[4]").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[6]/input").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[7]/button").click()




print("Test case 1: Approve survey")
approve_survey()
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/div")
    print("Test pass: Survey is approved by clicking show")
except:
    print("Test fail: error in approving survey.")















# Close the browser
driver.quit()
