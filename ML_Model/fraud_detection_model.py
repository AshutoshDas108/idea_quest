import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from flask import Flask, request, jsonify

# Generate a simulated dataset
np.random.seed(42)
num_samples = 1000
data = {
    'amount': np.random.rand(num_samples) * 1000,  # transaction amount
    'oldBalance': np.random.rand(num_samples) * 1000,  # sender's balance before transaction
    'newBalance': np.random.rand(num_samples) * 1000,  # sender's balance after transaction
    'is_fraud': np.random.randint(2, size=num_samples)  # 0 for non-fraud, 1 for fraud
}
df = pd.DataFrame(data)

# Preprocess the dataset
X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the logistic regression model
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Flask app to act as an intermediate API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    if not isinstance(dict(data), dict):
        return jsonify({"error": "Invalid input data format"}), 400
    
    amount = data.get('amount')
    oldBalance = data.get('oldBalance')
    newBalance = data.get('newBalance')

    # Validate inputs
    if amount is None or oldBalance is None or newBalance is None:
        return jsonify({'error': 'Invalid input data'}), 400

    # Data processing and prediction logic here
    X_new = np.array([[amount, oldBalance, newBalance]])
    X_new_scaled = scaler.transform(X_new)
    y_pred = model.predict(X_new_scaled)
    y_pred_prob = model.predict_proba(X_new_scaled)[:, 1]
    
    resp = ""
    if y_pred == 0:
        resp = 'SAFE TRANSACTION'
    else:
        resp = 'POTENTIAL FRAUD'
        
    
    return jsonify({
        "result" : resp
    })
    
    # return jsonify({
    #     'prediction': int(y_pred[0]),
    #     'probability': float(y_pred_prob[0])
    # })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)



