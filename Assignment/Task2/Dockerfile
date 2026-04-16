FROM python:3.8-slim

WORKDIR /app

COPY app.py index.html styles.css ./

RUN pip install flask redis

CMD python3 app.py

EXPOSE 5002