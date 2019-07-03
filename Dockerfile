FROM python:3.6.5-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN nosetests tests/spotify_api_tests.py 

CMD ["python", "app.py"]