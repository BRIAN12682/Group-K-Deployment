FROM python:slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /libapp

COPY  requirements.txt requirements.txt

COPY . .

# RUN apk update && apk add mysql-client
# RUN apt-get update && apt-get install -y default-mysql-client

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["Python", "manage.py", "runserver", "0.0.0.0:8000"]
