FROM python:3.11

WORKDIR /home/menu_project


RUN apt-get update && apt-get -y install libgpg-error-dev gcc netcat-openbsd

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
