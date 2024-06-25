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
import pickle

df_path = './dataset/final_dataset.csv'

def predict(model, test_set):
    predictions = model.predict(test_set)
    test_set["prediction"] = predictions
    
    return test_set

def train_and_test(df_path):

    # Balanced dataset
    df_balanced = pd.read_csv(df_path)

    # Separating numerical and categorical features
    NUMERICAL_FEATURES = [i for i in df_balanced.columns if df_balanced[i].dtype == 'int64'\
                        or df_balanced[i].dtype =='int32' \
                        or df_balanced[i].dtype =='float64']

    CATEGORICAL_FEATURES = [i for i in df_balanced.columns if df_balanced[i].dtype == 'object']

    last_column = df_balanced.shape[1]-1
    df_balanced.rename(columns={last_column: 'is_fraud'}, inplace=True)

    # Fixing datatype
    df_balanced[['is_fraud', 'age']] = df_balanced[['is_fraud', 'age']].astype('float64')

    # X = feature values, all the columns except the last column
    X = df_balanced.drop(columns = 'is_fraud')

    # y = target values, last column of the data frame
    y = df_balanced['is_fraud']

    # Encoding categorical features
    encoder = OrdinalEncoder()
    encoder.fit(X[CATEGORICAL_FEATURES])

    X[CATEGORICAL_FEATURES] = encoder.transform(X[CATEGORICAL_FEATURES])

    # Scaling dataset
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled = pd.DataFrame(X_scaled)

    

    # # X = feature values, all the columns except the last column
    # X = df_scaled.drop(columns = 'is_fraud')

    # # y = target values, last column of the data frame
    # y = df_scaled['is_fraud']

    # Spliting train and test - hold out
    x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # XGBoost classifier model
    xgb = XGBClassifier(objective='binary:logistic')
    xgb.fit(x_train, y_train)

    # Testing on test dataset
    predict(xgb, x_test)
    x_test["real"] = y_test

    print(classification_report(x_test['real'], x_test['prediction']))

    with open('xgboost_model.pkl', 'wb') as f:
        pickle.dump(xgb, f)

    # Save encoder and scaler using pickle
    with open('encoder.pkl', 'wb') as f:
        pickle.dump(encoder, f)

    with open('scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    # Prepare data to save in JSON
    data_to_save = {
        "encoder_path": "encoder.pkl",
        "scaler_path": "scaler.pkl",
        "categorical_features": CATEGORICAL_FEATURES
    }

    # Save to a JSON file
    with open('model_metadata.json', 'w') as json_file:
        json.dump(data_to_save, json_file)


train_and_test(df_path)



