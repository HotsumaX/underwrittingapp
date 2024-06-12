"""Module for multi-family property evaluation."""



def evaluate_multi_family(property_data):
    """
    Evaluate the value of a multi-family property.

    Args:
        property_data (dict): A dictionary containing the property details.

    Returns:
        float: The evaluated value of the property.
    """
    value = property_data['price'] * 0.85
    return value
