FROM python:3.8-slim

WORKDIR /app

COPY fraud_detection_model.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "fraud_detection_model.py"]
