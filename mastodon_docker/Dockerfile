FROM python:3.10-alpine
WORKDIR /app
COPY . /app
COPY ./nltk_data /usr/local/nltk_data
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "Mastodon_client.py"]
