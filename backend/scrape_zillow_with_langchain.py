import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from langchain.prompts import Prompt
from llama_index import Document, GPTVectorStoreIndex  # Correct import paths

class WebScrapingChain:
    def __init__(self):
        self.prompt = Prompt(template="Navigate to {url} and extract data.")

    def run(self, url):
        # Set up Selenium
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        
        # Fetch the webpage
        driver.get(url)
        time.sleep(3)  # Wait for the page to fully load

        # Get the page source
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # Close the driver
        driver.quit()

        # Extract data
        property_info = {}
        address = soup.find('h1', class_='ds-address-container')
        price = soup.find('span', class_='ds-value')

        property_info['address'] = address.get_text(strip=True) if address else 'Address not found'
        property_info['price'] = price.get_text(strip=True) if price else 'Price not found'

        return property_info

def scrape_zillow_listing(url):
    chain = WebScrapingChain()
    data = chain.run(url)

    # Indexing data with LlamaIndex
    documents = [Document(text=f"Address: {data['address']}, Price: {data['price']}")]
    index = GPTVectorStoreIndex.from_documents(documents)

    # Query the index to verify data
    query_engine = index.as_query_engine()
    results = query_engine.query('Find the address and price')
    return results

# Example usage
if __name__ == "__main__":
    url = 'https://www.zillow.com/homedetails/404-Cardinal-Dr-Clayton-NC-27520/69130415_zpid/'
    fields = scrape_zillow_listing(url)
    for result in fields:
        print(result.text)
