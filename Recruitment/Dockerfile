# Base Image
FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# set default environment variables
ENV PYTHONUNBUFFERED 1
# ENV LANG C.UTF-8
# ENV DEBIAN_FRONTEND=noninteractive 

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8080

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# install environment dependencies
RUN pip3 install --upgrade pip 
RUN pip3 install pipenv

# Install project dependencies
# RUN pipenv install --skip-lock --system --dev

EXPOSE 8080
CMD gunicorn Recruitment.wsgi:application --bind 0.0.0.0:$PORT