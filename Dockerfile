FROM python:3.6.5

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

ADD . /app

# ENTRYPOINT entrypoint.py
