FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD . /app/

ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8080