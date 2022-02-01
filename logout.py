import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
from termcolor import cprint
import colorama
colorama.init()

load_dotenv("sample.env") 
load_dotenv("personal.env")
USER = os.getenv('MY_USER') or os.getenv('USER')
PWD = os.getenv('MY_PWD') or os.getenv('PWD')
COMPANY = os.getenv('MY_COMPANY') or os.getenv('COMPANY')

print("USER", USER)
print("PWD", PWD)
print("COMPANY", COMPANY)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() # For maximizing window
driver.implicitly_wait(15) # gives an implicit wait for 20 seconds
driver.get("https://maxhr.myadrenalin.com/AdrenalinMax/#/")
print(driver.title)

try:
    userInputField = driver.find_element_by_id("txtID")
    userInputField.send_keys(USER)
    userInputField = driver.find_element_by_id("txtPwd")
    userInputField.send_keys(PWD)
    userInputField = driver.find_element_by_id("txtCompName")
    userInputField.send_keys(COMPANY)

    loginBtn = driver.find_element_by_id('lblLogin')
    driver.execute_script("arguments[0].click();", loginBtn)

    time.sleep(5) # Let the user actually see something!

    # attendanceBtn = driver.find_element_by_class_name('down_sign_popup')
    attendanceBtn = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle down_sign_popup']")
    attendanceBtn.click()

    time.sleep(5) # Let the user actually see something!

    attendanceBtn = driver.find_element(By.XPATH, "//button[@class='btn primary_cstm_btn btn-primary btn-sm green_color mr-2 ng-star-inserted']")
    attendanceBtn.click()

    time.sleep(5) # Let the user actually see something!

    attendanceBtn = driver.find_element_by_class_name('swal2-confirm')
    attendanceBtn.click()

    print(driver.current_url)
except Exception as e:
    cprint('Oh no an exceptional exception materializes. What do we do now?', 'red')
    print ('If you are already signed in, sign out first.')
    print (e)
    driver.close()
else:
    cprint('Logged Out - No exception occurred', 'green')
    time.sleep(5) # Let the user actually see something!
    driver.close()