FROM python:3.10-bullseye

WORKDIR /repeater

ADD requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py *.json ./

ENTRYPOINT ["python", "repeater.py"]
