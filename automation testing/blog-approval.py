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


print("blog approval feature test")

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
def approve_blog():
    driver.find_element(By.CSS_SELECTOR, "#sidenavAccordion > div.sb-sidenav-menu > div > a:nth-child(10)").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/nav/div[1]/div/div[6]/nav/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/table/tbody/tr[1]/td[5]/a").click()
    time.sleep(5)
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[4]/button").click()
    time.sleep(5)


def approve_blog2():
    time.sleep(5)
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[3]/input").click()
    time.sleep(5)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[4]/button").click()
    time.sleep(5)

def approve_blog3():

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/table/tbody/tr[1]/td[5]/a").click()
    time.sleep(5)

    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[2]/input").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[3]/input").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/form/div[11]/div[4]/button").click()
    time.sleep(5)





print("Test case 1: Approve a blog without clicking terms and conditions")
approve_blog()
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/div/ul/li")
    print("Test pass: Blog is not approved without clicking terms and condition.")
except:
    print("Test fail: Blog approved without clicking terms and conditions.")



print("Test case 2: Approve a blog by clicking terms and conditions but not show button")
approve_blog2()
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/table/tbody/tr[1]/td[4]")
    print("Test pass: Blog is approved by clicking terms and condition but status is hidden.")
except:
    print("Test fail: Blog approved without clicking terms and conditions.")



print("Test case 3: Approve a blog by clicking terms and conditions but and show button")
approve_blog3()
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div[2]")
    print("Test pass: Blog is approved by clicking terms and condition but status is show.")
except:
    print("Test fail: Blog approved without clicking terms and conditions.")


# Testing with null
# print("Testing with null Email")
# signup("", password, password_confirmation)
# time.sleep(5)
# try:
#     email_input = driver.find_element(By.NAME, "email")
#     if "required" in email_input.get_attribute("outerHTML"):
#         print("Test pass: email field is marked as required.")
# except:
#     print("Test failed: email field not marked as required.")















# Close the browser
driver.quit()
