FROM ubuntu:20.04

RUN apt-get update -y && \
  DEBIAN_FRONTEND="noninteractive" apt-get install -y build-essential checkinstall \ 
  libreadline-gplv2-dev libncursesw5-dev libssl-dev \
  libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev software-properties-common curl

RUN add-apt-repository ppa:deadsnakes/ppa -y

RUN apt-get install python3.11 python3.11-distutils -y
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

WORKDIR /app

COPY ./src /app/src
COPY ./templates /app/templates
COPY ./requirements.txt /app/requirements.txt

RUN python3.11 -m pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5004"]