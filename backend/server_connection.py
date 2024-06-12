"""
Module documentation
"""


import logging
import requests

    """
    Function documentation
    """
def get_server_status(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error("Error connecting to server: %s", e)
        return None
