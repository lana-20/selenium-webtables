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

print(num_of_rows)  # 7, including the headers (in the 1st row)
print(num_of_columns) # 4

# Read specific row and columns data
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data) # Master In Selenium

# Read all the rows and columns data
print("Printing all the rows and columns data")

for r in range(2, num_of_rows + 1):
	for c in range(1, num_of_columns + 1):
		data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
		print(data, end="   ")
	print()

# List books based on a condition
