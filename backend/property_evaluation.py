import json

def evaluate_property(property_data):
    report = ""

    # Extracting relevant details from the JSON data
    title = property_data.get('title', 'Unknown')
    address = property_data.get('address', 'Unknown')
    price = property_data.get('price', 'Unknown')
    year_built = property_data.get('year_built', 'Unknown')
    renovations = property_data.get('renovations', [])
    cap_rate = property_data.get('cap_rate', 'Unknown')
    price_per_sq_ft = property_data.get('price_per_sq_ft', 'Unknown')
    price_per_unit = property_data.get('price_per_unit', 'Unknown')
    zoning = property_data.get('zoning', 'Unknown')

    # Basic information
    report += f"Property Title: {title}\n"
    report += f"Address: {address}\n"
    report += f"Price: {price}\n"
    report += "\n### Renovation Quality:\n"

    if renovations:
        report += "The property has undergone the following renovations:\n"
        for renovation in renovations:
            report += f" - {renovation}\n"
    else:
        report += "No renovation information provided.\n"

    # Building Age
    report += "\n### Building Age:\n"
    report += f"Built in {year_built}, the building might have underlying issues typical of older constructions despite recent renovations.\n"

    # Market Performance
    report += "\n### Market Performance:\n"
    report += f"Cap Rate: {cap_rate}\n"
    report += f"Price/Sq Ft: {price_per_sq_ft}\n"
    report += f"Price/Unit: {price_per_unit}\n"

    # Location
    report += "\n### Location:\n"
    address_parts = address.split(',')
    if len(address_parts) > 2:
        report += f"The property's location in {address_parts[-2].strip()} is a growing market with a strong rental demand.\n"
    else:
        report += "The property's location is not fully detailed in the address provided.\n"

    # Potential Concerns
    report += "\n### Potential Concerns:\n"
    report += "1. Remaining Older Components: Despite renovations, some elements (e.g., plumbing, foundation) might not have been updated. These can lead to future repairs.\n"
    report += f"2. Zoning Restrictions: Ensure the zoning ({zoning}) allows for intended use and any future expansions or modifications.\n"
    report += "3. Tenant Management: Managing a multifamily property requires consistent oversight. Consider the time and resources needed for property management.\n"
    report += "4. Economic Fluctuations: Monitor economic conditions and rental market trends in the area to ensure continued demand and rental income stability.\n"

    # Recommendations
    report += "\n### Recommendations:\n"
    report += "1. Conduct a thorough inspection to uncover any hidden issues, especially in areas not covered by the recent renovations.\n"
    report += "2. Compare with similar properties in terms of price, cap rate, and amenities to ensure the investment is competitively positioned.\n"
    report += "3. Analyze the financials in detail, considering both current and projected income and expenses, to validate the investment potential.\n"

    return report

if __name__ == "__main__":
    with open('crexi_listing.json', 'r') as f:
        property_data = json.load(f)
        report = evaluate_property(property_data)
        print(report)

        with open('property_evaluation_report.txt', 'w') as report_file:
            report_file.write(report)