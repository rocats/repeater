FROM python:3.10-bullseye

WORKDIR /repeater

ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD *.py .

ENTRYPOINT ["python", "repeater.py"]
