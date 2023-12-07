FROM python:3.8

RUN mkdir -p /app/code
WORKDIR /app/code
COPY . .

RUN pip3 install -r requirements.txt

