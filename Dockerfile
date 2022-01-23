FROM python:3.8-buster as builder
WORKDIR /opt/app
COPY requirements.lock /opt/app
RUN pip3 install -r requirements.lock

COPY lib/ /scripts/
COPY fetch_trades.py /scripts/fetch_trades.py

ENTRYPOINT ["python3", "/scripts/fetch_trades.py"]