#!/bin/bash

# Navigate to the backend directory
cd backend

# Create logging_config.py file
cat <<EOL > logging_config.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )
EOL

# Create server_connection.py file
cat <<EOL > server_connection.py
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
EOL

# Create scrape_zillow.py file
cat <<EOL > scrape_zillow.py
import time
import random
from selenium import webdriver
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def scrape_zillow_listing(url):
    logger.info('Starting scrape for URL: %s', url)
    driver = webdriver.Chrome()  # Ensure WebDriver is properly set up
    try:
        driver.get(url)
        time.sleep(random.uniform(2, 5))
        content = driver.page_source
        logger.info('Scraping successful')
        return content
    except Exception as e:
        logger.error('Error during scraping: %s', e)
        raise
    finally:
        driver.quit()
EOL

# Navigate back to the root directory
cd ..

# Create LOGGING.md file
cat <<EOL > LOGGING.md
## Logging and Error Handling

### Logging Configuration
- Logs are configured using the \`logging_config.py\` module.
- Logs are written to both the console and \`app.log\` file.

### Usage
- Import and setup logging in your module:
  \`\`\`python
  import logging
  from logging_config import setup_logging

  setup_logging()
  logger = logging.getLogger(__name__)
  \`\`\`

### Error Handling
- Use try-except blocks to catch and log errors.
- Ensure meaningful error messages are raised or returned.
EOL

echo "Script executed successfully. Please run 'python3 backend/scrape_zillow.py' to validate the logging and error handling implementation."