FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/
COPY city_to_city_pop.json /app/
COPY merchant_to_category.json /app/
COPY model_metadata.json /app/
COPY scaler.pkl /app/
COPY encoder.pkl /app/
COPY xgboost_model.pkl /app/
COPY model.py /app/
COPY infer.py /app/

EXPOSE 5000

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "infer.py"]


# FROM python:3.8-slim

# WORKDIR /app

# COPY fraud_detection_model.py /app/
# COPY requirements.txt /app/

# RUN pip install -r requirements.txt

# CMD ["python", "fraud_detection_model.py"]
