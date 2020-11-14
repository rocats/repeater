FROM python:3.7-alpine
ADD . /repeater
WORKDIR /repeater
RUN apk add --no-cache gcc g++ linux-headers libffi-dev openssl-dev
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "repeater.py"]