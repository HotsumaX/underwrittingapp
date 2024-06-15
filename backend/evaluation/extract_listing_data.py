import json

def get_listings():
    with open('crexi_listing.json') as f:
        listings = json.load(f)
    return listings