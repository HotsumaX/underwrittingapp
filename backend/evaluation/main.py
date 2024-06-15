# main.py

import extract_listing_data
import store_data
import analyze_data
import visualize_data

# Extract data from the JSON file
listings = extract_listing_data.extract_listing_data('crexi_listing.json')

# Store the extracted data into the database
store_data.store_data(listings)

# Perform analysis on the stored data
analysis_results = analyze_data.analyze_data()

# Visualize the analysis results
visualize_data.visualize_data(analysis_results)