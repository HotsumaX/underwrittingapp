"""
Module documentation
"""


import logging
import requests
from bs4 import BeautifulSoup

    """
    Function documentation
    """
def scrape_site(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.RequestException as e:
        logging.error("Error scraping site: %s", e)
        return None
