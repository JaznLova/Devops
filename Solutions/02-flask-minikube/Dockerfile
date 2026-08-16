FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

EXPOSE 15000
USER 65532:65532
CMD ["gunicorn", "--bind", "0.0.0.0:15000", "app:app"]
