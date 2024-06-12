import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_driver():
    options = Options()
    options.headless = True
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def fetch_zillow_page(url):
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)  # Allow some time for the page to load

    try:
        # Here you might need to wait or interact with CAPTCHA if necessary
        html_content = driver.page_source
        driver.quit()
        return html_content
    except Exception as e:
        driver.quit()
        logger.error(f"Error loading key elements: {e}")
        return f"Error loading key elements after CAPTCHA: {e}"

@app.route('/api/sample_zillow', methods=['GET'])
def sample_zillow():
    url = request.args.get('url')
    html_content = fetch_zillow_page(url)
    return jsonify({"html_content": html_content})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)