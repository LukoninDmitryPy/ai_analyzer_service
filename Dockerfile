FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
