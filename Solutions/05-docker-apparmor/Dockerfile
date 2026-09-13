FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir Flask==3.1.2
COPY app.py .

EXPOSE 5000
USER 65532:65532
CMD ["python", "app.py"]
