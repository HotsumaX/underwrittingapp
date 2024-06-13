"""Module to scrape websites."""

from selenium import webdriver

from selenium.webdriver.common.by import By
def scrape_site(url):
    """
    Scrape the site for its title.

    Args:
        url (str): The URL of the site to scrape.

    Returns:
        str: The title of the site.
    """
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        title = driver.find_element(By.TAG_NAME, 'title').text
        return title
    finally:
        driver.quit()
