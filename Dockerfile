#                            _
#  _ __ ___ _ __   ___  __ _| |_ ___ _ __
# | '__/ _ \ '_ \ / _ \/ _` | __/ _ \ '__|
# | | |  __/ |_) |  __/ (_| | ||  __/ |
# |_|  \___| .__/ \___|\__,_|\__\___|_|
#          |_|
#
#  https://github.com/yqlbu/repeater
#
#  Copyright (C) 2023 @yqlbu
#
#  This is a self-hosted software, liscensed under the MIT License.
#  See /License for more information.

# === Build Stage === #
FROM python:3.10-bullseye as builder

WORKDIR /app

ADD ./ci/prod.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY *.py ./
RUN pyinstaller repeater.py

# === Prod Stage === #

FROM debian:bullseye-slim as prod

WORKDIR /app

COPY --from=builder /app/dist/repeater/ ./
COPY *.json ./

RUN chmod +x ./repeater

CMD ["./repeater"]
