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


print("Student Signup Feature Test")

cb_number = "CB011345"
batch = "IF23A1SE"
student_degree = "BSc in Computer Science"
name = "Fernando"
email = "fernando@gmail.com"
password = "12345678"
password_confirmation = "12345678"


url = "https://group-6.laravelsrilanka.com/"

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url)

# Function to login with provided credentials
def signup(cb_number,batch,student_degree,name, email, password, password_confirmation):
    driver.find_element(By.NAME, "cb_number").clear()
    driver.find_element(By.NAME, "cb_number").send_keys(cb_number)

    driver.find_element(By.NAME, "batch").clear()
    driver.find_element(By.NAME, "batch").send_keys(batch)

   

    driver.find_element(By.NAME, "student_degree").clear()
    driver.find_element(By.NAME, "student_degree").send_keys(student_degree)

    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
 
  
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)

    driver.find_element(By.NAME, "password_confirmation").clear()
    driver.find_element(By.NAME, "password_confirmation").send_keys(password_confirmation)

    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[17]/button").click()


def signup_with_error(name, email, student_id, batch, password, password_confirmation):
    driver.find_element(By.NAME, "name").clear()
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "student_id").clear()
    driver.find_element(By.NAME, "student_id").send_keys(student_id)
    driver.find_element(By.NAME, "batch").clear()
    driver.find_element(By.NAME, "batch").send_keys(batch)
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password_confirmation").clear()
    driver.find_element(By.NAME, "password_confirmation").send_keys(password_confirmation)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[7]/button").click()




userbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='flex flex-row items-center w-full px-4 py-2 mt-2 text-sm font-semibold text-left bg-transparent rounded-lg dark-mode:bg-transparent dark-mode:focus:text-white dark-mode:hover:text-white dark-mode:focus:bg-gray-600 dark-mode:hover:bg-gray-600 md:w-auto md:inline md:mt-0 md:ml-4 hover:text-gray-900 focus:text-gray-900 hover:bg-gray-200 focus:bg-gray-200 focus:outline-none focus:shadow-outline']")))
userbutton.click()


signupbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div/div/div/a[2]")))
signupbutton.click()



# Testing with incorrect credentials - CB number
print("Test case 1: Testing with incorrect CB number / empty...")
signup("",batch,student_degree,name, email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/ul").text
    if welcome_message:
        print("Test pass: CB number feild id marked as required ")
except:
    print("Test failed: Welcome message not found.")


# Testing with incorrect credentials - Batch
print("Test case 2: Testing with incorrect Batch / empty...")
signup(cb_number,"",student_degree,name, email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[3]/ul").text
    if welcome_message:
        print("Test pass: Batch field id marked as required ")
except:
    print("Test failed: Welcome message not found.")



# Testing with incorrect credentials - Degree programme
print("Test case 3 :Testing with incorrect School / empty...")
signup(cb_number,batch,"",name, email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[6]/ul").text
    if welcome_message:
        print("Test pass: Degree feild id marked as required ")
except:
    print("Test failed: Welcome message not found.")



# Testing with incorrect credentials - Name
print("Test case 4: Testing with incorrect Name / empty...")
signup(cb_number,batch,student_degree,"", email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[13]/ul").text
    if welcome_message:
        print("Test pass: Name feild id marked as required ")
except:
    print("Test failed: Welcome message not found.")



# Testing with incorrect credentials - Email
print("Test case 5: Testing with incorrect Email / empty...")
signup(cb_number,batch,student_degree,name, "", password, password_confirmation)
time.sleep(5)
try:
    email_input = driver.find_element(By.NAME, "email")
    if "required" in email_input.get_attribute("outerHTML"):
        print("Test pass: email field is marked as required.")
except:
    print("Test failed: email field not marked as required.")
    



# Testing with incorrect credentials - same student ID
print("Test case 6: Testing with same student_ID ...")
signup("CB011331",batch,student_degree,name, email, password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[2]/ul").text
    if welcome_message:
        print("Test pass: Cannot register with same student ID.")
except:
    print("Test failed: Welcome message not found")


# Testing with incorrect credentials - same student Email
print("Test case 7: Testing with same student email ...")
signup(cb_number,batch,student_degree,name, "student2@gmail.com", password, password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[14]/ul").text
    if welcome_message:
        print("Test pass: Cannot register with same student ID.")
except:
    print("Test failed: Welcome message not found")



# Testing with incorrect credentials - different passwords
print("Test case 8 :Testing with different passwords ...")
signup(cb_number,batch,student_degree,name, email, "123456789", password_confirmation)
time.sleep(5)
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form/div[15]/ul/li").text
    if welcome_message:
        print("Test pass: Cannot register with two different passwords.")
except:
    print("Test failed: Welcome message not found")




# Testing with correct credentials
print("Test case 9: Testing with correct credentials...")
signup(cb_number,batch,student_degree,name, email, password, password_confirmation)
time.sleep(5)  # Wait for 5 seconds

# Check if logged in successfully
try:
    welcome_message = driver.find_element(By.XPATH, "/html/body/div[1]/div").text
    time.sleep(5)
    if welcome_message:
        print("Test pass: Signed-in successfully with correct credentials.")
except:
    print("Test failed: Welcome message not found.")

# Close the browser
driver.quit()
