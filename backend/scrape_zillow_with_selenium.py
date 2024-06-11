import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_zillow_listing(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    time.sleep(3)  # Wait for the page to fully load

    try:
        # Extract the address
        address = driver.find_element(By.XPATH, "//h1[contains(@class, 'ds-address-container')]").text
    except:
        address = "Address not found"

    try:
        # Extract the price
        price = driver.find_element(By.XPATH, "//span[contains(@class, 'ds-value')]").text
    except:
        price = "Price not found"
    
    driver.quit()

    return {
        "address": address,
        "price": price
    }
