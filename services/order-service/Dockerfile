FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY services/order-service/ .

EXPOSE 8002

ENV USER_SERVICE_URL=http://user-service:8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]
