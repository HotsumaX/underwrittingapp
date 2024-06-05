from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from scrape_zillow import scrape_zillow_data
from scrape_crexi import scrape_crexi_data
from gpt_code_review import review_code

app = Flask(__name__)
CORS(app)

openai.api_key = 'your_openai_api_key'

@app.route('/api/scrape_zillow', methods=['GET'])
def scrape_zillow():
    data = scrape_zillow_data()
    return jsonify(data)

@app.route('/api/scrape_crexi', methods=['GET'])
def scrape_crexi():
    data = scrape_crexi_data()
    return jsonify(data)

@app.route('/api/review_code', methods=['POST'])
def review_code_endpoint():
    code = request.json.get('code')
    review = review_code(code)
    return jsonify(review)

if __name__ == '__main__':
    app.run()
