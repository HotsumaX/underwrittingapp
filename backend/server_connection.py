import requests
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def connect_to_server(url):
    logger.info('Attempting to connect to server at %s', url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        logger.info('Successfully connected to server')
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error('Error connecting to server: %s', e)
        raise
