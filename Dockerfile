FROM python:3.6.5

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD . /app

CMD ["python", "main.py" ]
