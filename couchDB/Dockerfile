FROM python:3.9

WORKDIR /backend

COPY . /backend

RUN pip install couchdb;\
    pip install flask;\
    pip install flask-restful;\
    pip install flask_script;\
    pip install flask_migrate;\
    pip install flask-cors

EXPOSE 8080

CMD ["python", "./Flask/app.py"]