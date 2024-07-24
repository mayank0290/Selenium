# Import necessary modules from selenium and other required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Specify the path to the ChromeDriver executable
service = Service(executable_path="chromedriver.exe")

# Initialize the Chrome WebDriver with the specified service
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game website
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Define IDs for the big cookie and the cookies count
cookie_id = "bigCookie"
cookies_id = "cookies" 

# Define prefixes for the product price and product elements
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait until the "English" language option appears and click it
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait until the big cookie element is present
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(By.ID, cookie_id)
)

# Find the big cookie element
cookie = driver.find_element(By.ID, cookie_id)

# Infinite loop to continuously click the cookie and buy upgrades
while True: 
    # Click the big cookie
    cookie.click()
    
    # Get the current number of cookies
    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)
    
    # Loop through the first four products to check if they can be purchased
    for i in range(4): 
        # Get the price of the current product
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        
        # Skip the product if its price is not a digit (e.g., if it's "???")
        if not product_price.isdigit():
            continue
        
        # Convert the product price to an integer
        product_price = int(product_price)

        # If the current number of cookies is enough to buy the product
        if cookies_count >= product_price:
            # Find the product element and click it to purchase
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break  # Break the loop after buying one product to start clicking the cookie again
