FROM python:3.8.5

RUN mkdir /code
RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000
