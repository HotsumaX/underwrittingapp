from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/sample_zillow', methods=['GET'])
def sample_zillow():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)
        html_content = driver.page_source
        return jsonify({'html_content': html_content})
    except Exception as e:
        logging.error('Error loading key elements: %s', e)
        return jsonify({'html_content': f'Error loading key elements after CAPTCHA: {str(e)}'})
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True)