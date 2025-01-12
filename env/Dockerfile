FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/
ENV NAME World

RUN apt-get update \
    && pip install --no-cache-dir --default-timeout=300 --upgrade pip \
    && pip install --no-cache-dir --default-timeout=300 -r requirements.txt \
    && apt-get clean

COPY . /app

RUN chown -R root  /app
USER root
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
ENTRYPOINT ["python"]
