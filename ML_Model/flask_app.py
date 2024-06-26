from flask import Flask, request, jsonify
import requests
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)
    logger.error(f'data : {data}')
    # Ensure data is a dictionary and JSON serializable
    if not isinstance(dict(data), dict):
        logger.error('JSON serialization error')
        return jsonify({"error": "Invalid input data format"}), 400

    try:
        # Forward data to the machine learning model in the Docker container
        logger.error('INSIDE TRY BLOCK')
        url = 'http://rpi_emulator:5001/predict'
        #url = 'http://127.0.0.1:5000/predict'
        logger.error(f'calling the {url}')
        response = requests.post(url, json=data)
        logger.error(f'got the response: {response}')
        #response.raise_for_status() 
        logger.error(f'{response.json()}')
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logger.error('INSIDE EXCEPT BLOCK')
        logger.error(f'Error : {str(e)}')
        return jsonify({"error in calling Model@5001": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
