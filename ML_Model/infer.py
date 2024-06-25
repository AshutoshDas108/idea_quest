import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import json
from flask import Flask, request, jsonify
import pickle
import logging

logger = logging.getLogger(__name__)

# amount, merchant, dob, city, state, lat, long
# object:


# {
#     amount: float
#     merchant: string
#     age: int
#     city: string
#     state: string
#     lat: float
#     long: float
#     hour: int
    
# }


# Function to get time of day
def get_tod(hour):
    if 4 < hour <= 12:
        ans = 'morning'
    elif 12 < hour <= 20:
        ans = 'afternoon'
    elif hour <= 4 or hour > 20:
        ans = 'night'
    return ans


def preprocess(data,encoder,scaler,CATEGORICAL_FEATURES):
    with open('merchant_to_category.json', 'r') as json_file:
        merchant_to_category = json.load(json_file)
    merchant_category = merchant_to_category[data["merchant"]]

    with open('city_to_city_pop.json', 'r') as json_file:
        city_to_city_pop = json.load(json_file)
    city_pop = city_to_city_pop[data["city"]]

    time_category = get_tod(data["hour"])

    new_data = {
        'hour_transaction': [time_category],
        'category': [merchant_category],
        'amt': [data["amount"]],
        'city': [data["city"]],
        'state': [data["state"]],
        'lat': [data["lat"]],
        'long': [data["long"]],
        'city_pop': [city_pop],
        'age': [data["age"]],
    }


    # # Parse JSON objects
    # new_data = json.loads(new_data)

    # Convert JSON objects to DataFrame
    df = pd.DataFrame(new_data)

    df[CATEGORICAL_FEATURES] = encoder.transform(df[CATEGORICAL_FEATURES])
    df_scaled = scaler.transform(df)
    df_scaled = pd.DataFrame(df_scaled)

    return df_scaled




app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def infer():
    
    data = request.json 
    logger.info(data)
    
    # Ensure data is a dictionary and JSON serializable
    if not isinstance(dict(data), dict):
        return jsonify({"error": "Invalid input data format"}), 400
    
    
     # Load the JSON file
    with open('model_metadata.json', 'r') as json_file:
        m_data = json.load(json_file)
        
    
    logger.info(m_data)

    # Load the encoder and scaler using the paths stored in the JSON file
    with open(m_data['encoder_path'], 'rb') as f:
        loaded_encoder = pickle.load(f)

    with open(m_data['scaler_path'], 'rb') as f:
        loaded_scaler = pickle.load(f)

    with open('xgboost_model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)

    # Access the categorical features
    CATEGORICAL_FEATURES = m_data['categorical_features']

    # input_data = {
    #     "amount" : 100,
    #     "merchant" : "fraud_Kirlin and Sons",
    #     "age" : 35,
    #     "city" : "Columbia",
    #     "state" : "SC",
    #     "lat" : 33.9659,
    #     "long" : -80.9355, 
    #     "hour" : 12
    # }

    preprocessed_data = preprocess(data=data,encoder=loaded_encoder,scaler=loaded_scaler,CATEGORICAL_FEATURES=CATEGORICAL_FEATURES)

    y_pred = loaded_model.predict(preprocessed_data)

    resp = ""
    if y_pred == 0:
        resp = 'SAFE TRANSACTION'
    else:
        resp = 'POTENTIAL FRAUD'
    
    #return resp
    return jsonify({
        "result" : resp
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)





# def main():
    
#     # Load the JSON file
#     with open('model_metadata.json', 'r') as json_file:
#         data = json.load(json_file)

#     # Load the encoder and scaler using the paths stored in the JSON file
#     with open(data['encoder_path'], 'rb') as f:
#         loaded_encoder = pickle.load(f)

#     with open(data['scaler_path'], 'rb') as f:
#         loaded_scaler = pickle.load(f)

#     with open('xgboost_model.pkl', 'rb') as f:
#         loaded_model = pickle.load(f)

#     # Access the categorical features
#     CATEGORICAL_FEATURES = data['categorical_features']

#     input_data = {
#         "amount" : 100,
#         "merchant" : "fraud_Kirlin and Sons",
#         "age" : 35,
#         "city" : "Columbia",
#         "state" : "SC",
#         "lat" : 33.9659,
#         "long" : -80.9355, 
#         "hour" : 12
#     }

#     result = infer(loaded_model,input_data,loaded_encoder,loaded_scaler,CATEGORICAL_FEATURES)
#     return result