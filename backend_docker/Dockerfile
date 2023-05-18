FROM python:3.8-slim
WORKDIR /app

COPY .  /app
RUN pip install -r requirements.txt

EXPOSE 8081
CMD ["python3", "backend.py"]