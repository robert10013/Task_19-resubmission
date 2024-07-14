import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
paths = r"D:\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.maximize_window()
username=driver.find_element(By.ID,"user-name")
time.sleep(4)
username.click()
username.send_keys("standard_user")
password=driver.find_element(By.ID,"password")
password.click()
password.send_keys("secret_sauce")
logins=driver.find_element(By.ID,"login-button")
logins.click()