FROM python:3.7-alpine
WORKDIR /repeater
RUN apk add --no-cache gcc g++ linux-headers libffi-dev openssl-dev
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "repeater.py"]