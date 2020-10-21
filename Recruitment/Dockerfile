FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD . /app/

ENV PYTHONUNBUFFERED 1

# ENV PORT=8080
# RUN apt-get update && apt-get install -y libpq-dev
# RUN apk update && apk add libpq
# RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
# RUN apt-get install --virtual .build-deps gcc python-dev musl-dev postgresql-dev

RUN pip3 install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8080
# CMD gunicorn Recruitment.wsgi:application --bind 0.0.0.0:8080