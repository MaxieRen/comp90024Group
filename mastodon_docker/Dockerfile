FROM python:3.10-alpine
ENV DB_USERNAME=admin
ENV DB_PASSWORD=password
ENV DB_NAME=mastodon_social_cleandata
ENV DB_IP=172.26.135.248
ENV MASTODON_SERVER=aus.social
ENV MASTODON_TOKEN=AvLtf57hHjGtSP5Qq_t-UyAfVABievlLY9Toba3RkZ8
WORKDIR /app
COPY . /app
COPY ./nltk_data /usr/local/nltk_data
RUN pip install -r requirements.txt
RUN chmod +x Mastodon_client.py
CMD ["sh", "-c", "python3 ./Mastodon_client.py --user ${DB_USERNAME} --password ${DB_PASSWORD} --dbName ${DB_NAME} --ip ${DB_IP} --server ${MASTODON_SERVER} --token ${MASTODON_TOKEN}"]


