FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY delivery_metrics.py .

EXPOSE 8000
USER 65532:65532
CMD ["python", "delivery_metrics.py"]
