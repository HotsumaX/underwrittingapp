"""Module for single-family property evaluation."""
    
    
    def evaluate_single_family(property_data):
    """
    Evaluate the value of a single-family property.
    
    Args:
    property_data (dict): A dictionary containing the property details.
    
    Returns:
    float: The evaluated value of the property.
    """
    value = property_data['price'] * 0.8
    return value