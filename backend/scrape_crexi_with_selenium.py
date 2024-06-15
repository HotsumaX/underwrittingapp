from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import logging
import time

# Set up logging
logging.basicConfig(filename='crexi_scraping.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1200")

# Initialize the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to scrape CREXi website
def scrape_crexi():
    try:
        logging.info("Navigating to CREXi website.")
        driver.get('https://www.crexi.com/properties')
        
        # Wait for the main container to load
        wait = WebDriverWait(driver, 20)
        main_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'crx-search-results')))
        logging.info("Main container loaded.")
        
        # Scroll and load more listings
        properties = []
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to load more listings
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for more listings to load
            
            # Find individual listings within the main container
            listings = main_container.find_elements(By.CLASS_NAME, 'result-card')
            logging.info(f"Found {len(listings)} listings.")
            
            for listing in listings:
                try:
                    title = listing.find_element(By.CLASS_NAME, 'result-card-title').text
                    address = listing.find_element(By.CLASS_NAME, 'result-card-address').text
                    price = listing.find_element(By.CLASS_NAME, 'result-card-price').text
                    properties.append({
                        'title': title,
                        'address': address,
                        'price': price
                    })
                    logging.info(f"Extracted listing: {title}, {address}, {price}")
                except Exception as e:
                    logging.error(f"Error extracting details from listing: {e}")
            
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        # Save the scraped data to a JSON file
        with open('crexi_properties.json', 'w') as f:
            json.dump(properties, f)
        
        logging.info(f"Scraped data saved to crexi_properties.json, found {len(properties)} listings")

    except Exception as e:
        logging.error(f"Error during scraping: {e}")
    finally:
        driver.quit()
        logging.info("Driver quit.")

if __name__ == "__main__":
    scrape_crexi()