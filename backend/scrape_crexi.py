import requests
from bs4 import BeautifulSoup

def scrape_crexi_data():
    url = 'https://www.crexi.com/properties'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    properties = []
    for listing in soup.find_all('div', {'class': 'property-item'})):
        address = listing.find('div', {'class': 'property-address'}).text if listing.find('div', {'class': 'property-address'}) else 'N/A'
        price = listing.find('div', {'class': 'property-price'}).text if listing.find('div', {'class': 'property-price'}) else 'N/A'
        properties.append({'address': address, 'price': price})

    return properties
