FROM python:3.11
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./src /app/src
COPY ./.env /app/.env
CMD ["uvicorn", "src.main:api", "--host", "0.0.0.0", "--port", "80"]