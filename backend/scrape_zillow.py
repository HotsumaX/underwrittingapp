import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebScrapingChain:
    def __init__(self, retries=3):
        self.retries = retries

    def run(self, url):
        for attempt in range(self.retries):
            try:
                logger.info(f"Attempt {attempt + 1} to scrape {url}")
                
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")
                options.add_argument("--disable-blink-features=AutomationControlled")
                options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
                
                driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
                
                driver.get(url)
                time.sleep(random.uniform(2, 5))  # Random delay to simulate human behavior
                
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                
                driver.quit()
                
                property_info = {}
                address = soup.find('h1', {'class': 'ds-address-container'})
                price = soup.find('span', {'class': 'ds-value'})
                
                property_info['address'] = address.get_text(strip=True) if address else 'Address not found'
                property_info['price'] = price.get_text(strip=True) if price else 'Price not found'
                
                return property_info
            
            except Exception as e:
                logger.error(f"Error on attempt {attempt + 1}: {str(e)}", exc_info=True)
                if attempt < self.retries - 1:
                    time.sleep(random.uniform(3, 6))  # Wait a bit before retrying
                else:
                    raise e

def scrape_zillow_listing(url):
    chain = WebScrapingChain()
    data = chain.run(url)
    return data

# Example usage
if __name__ == "__main__":
    url = 'https://www.zillow.com/homedetails/404-Cardinal-Dr-Clayton-NC-27520/69130415_zpid/'
    fields = scrape_zillow_listing(url)
    print(fields)
