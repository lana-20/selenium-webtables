from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.common.by import By

serv_obj = Service("...chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Count the number of rows and columns
num_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
num_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th"))
