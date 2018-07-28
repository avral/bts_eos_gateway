FROM python:3.6.5

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

run curl -sL https://deb.nodesource.com/setup_10.x | bash -
run apt-get install -y nodejs
run npm install --save tcjs


EXPOSE 8000

ADD . /app

# ENTRYPOINT entrypoint.py
