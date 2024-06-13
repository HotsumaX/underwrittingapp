"""
Module documentation
"""

"""
Module documentation
"""


import time

import random
from selenium import webdriver

import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

    """
    Function documentation
    """
    """
    Function documentation
    """

def scrape_zillow_listing(url):
    logger.info('Starting scrape for URL: %s', url)
    driver = webdriver.Chrome()  # Ensure WebDriver is properly set up
    try:
        driver.get(url)
        time.sleep(random.uniform(2, 5))
        content = driver.page_source
        logger.info('Scraping successful')
        return content
    except Exception as e:
        logger.error('Error during scraping: %s', e)
        raise
    finally:
        driver.quit()
