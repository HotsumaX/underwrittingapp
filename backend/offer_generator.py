"""Module to generate property offers."""

def generate_offer(property_data, evaluation):
    """
    Generate an offer based on the property data and evaluation.

    Args:
        property_data (dict): A dictionary containing the property details.
        evaluation (float): The evaluated value of the property.

    Returns:
        float: The offer price.
    """
    offer_price = evaluation - (property_data['price'] * 0.1)
    return offer_price
