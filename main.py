from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service = service)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

driver.get("https://www.google.com")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.clear()

input_element.send_keys("Github" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech with tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech with tim")
link.click()

time.sleep(6)

driver.quit()
