FROM python:3.12-slim

WORKDIR /app

# Salin Flask app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan Flask
CMD ["python3", "app.py"]
