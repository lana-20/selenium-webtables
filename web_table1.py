from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.common.by import By

serv_obj = Service("...chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
