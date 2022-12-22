# Bonnie Garcia's WebDriver Manager for Selenium 4 -> update svc object with ChromeDriverManager()
# https://pypi.org/project/webdriver-manager/
# https://bonigarcia.dev/webdrivermanager/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Admin -> User Management -> Users
wait = driver.WebDriverWait(driver, 5)
wait.until(EC.element_to_be_present((By.XPATH, "//li//a//span"))).click()   # Admin

driver.find_element(By.XPATH, "//nav//li/span").click()   # User Management
driver.find_element(By.CSS_SELECTOR, "a[role='menuitem']").click()  # Users

# total Number of rows in a table
rows = len(driver.find_elements(By.XPATH, "//*[@class='oxd-table-body']/div/div"))
print("total Number of rows:", rows)

# number of enabled employees
count = 0
for r in range(1, rows + 1):
	status = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[5]")).text
	if status == "Enabled":
		count += 1
print("Total number of users:", rows)
print("Number of enabled users:", count)
print("Number of disabled users:", (rows - count))

# print user names and roles if the user role is ESS
for r in range(1, rows + 1):
	role = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[3]")).text
	username = driver.find_element(By.XPATH, "//*[@class='oxd-table-body']/div["+str(r)+"]/div/div[2]")).text
	if role == "ESS":
		print(username, role)

driver.close()
