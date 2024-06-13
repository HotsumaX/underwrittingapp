from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/example', methods=['GET'])
def example_route():
    return jsonify({"message": "This is an example route"}), 200

@app.route('/api/reset_connection', methods=['POST'])
def reset_connection():
    # Implement your reset connection logic here
    return jsonify({"status": "connection reset"}), 200

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)