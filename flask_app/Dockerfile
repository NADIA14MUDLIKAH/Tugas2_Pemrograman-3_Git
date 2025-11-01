# Gunakan base image Python
FROM python:3.12-slim

# Set working directory di dalam container
WORKDIR /app

# Copy semua folder ke dalam container
COPY flask_app /app
COPY matrix_regression /app/matrix_regression
COPY data /app/data

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask
EXPOSE 5000

# Jalankan Flask
CMD ["python", "app.py"]

