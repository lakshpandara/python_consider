FROM python:3.7

RUN pip install Authlib requests Flask-SSLify Flask gunicorn firebase_admin flask-restful Flask-Dance

COPY src/ app/
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app