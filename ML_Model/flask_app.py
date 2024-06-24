from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    # Ensure data is a dictionary and JSON serializable
    if not isinstance(dict(data), dict):
        return jsonify({"error": "Invalid input data format"}), 400

    try:
        # Forward data to the machine learning model in the Docker container
        url = 'http://rpi_emulator:5001/predict'
        response = requests.post(url, json=data)
        return response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error in calling Model@5001": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
