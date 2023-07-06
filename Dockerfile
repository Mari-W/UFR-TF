FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip

WORKDIR /app

COPY ./src /app/src
COPY ./templates /app/templates
COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5004"]