FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install flask numpy

EXPOSE 5000
CMD ["python", "flask_app/app.py"]
