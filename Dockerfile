FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file proyek
COPY . .

# Pastikan folder utama dikenali Python sebagai module path
ENV PYTHONPATH=/app

WORKDIR /app/flask_app2
CMD ["python", "app.py"]

