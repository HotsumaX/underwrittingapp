"""Module to scrape Zillow using Selenium."""

from selenium import webdriver

from selenium.webdriver.common.by import By

def scrape_zillow(url):
    """
    Scrape Zillow for price and address.

    Args:
        url (str): The URL of the Zillow listing.

    Returns:
        dict: A dictionary containing the price and address.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        price = driver.find_element(By.CLASS_NAME, 'price').text
        address = driver.find_element(By.CLASS_NAME, 'address').text
        return {
            'price': price,
            'address': address
        }
    finally:
        driver.quit()
