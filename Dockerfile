FROM python:3.9-slim-bullseye
WORKDIR /repeater
RUN apt update && apt install -y build-essential libffi-dev libssl-dev libssl-dev python-dev
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "repeater.py"]
