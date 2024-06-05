import requests
from bs4 import BeautifulSoup

def scrape_zillow_data():
    url = 'https://www.zillow.com/homes/for_sale/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    properties = []
    for listing in soup.find_all('article'):
        address = listing.find('address').text if listing.find('address') else 'N/A'
        price = listing.find('span', {'class': 'price'}).text if listing.find('span', {'class': 'price'}) else 'N/A'
        properties.append({'address': address, 'price': price})

    return properties
