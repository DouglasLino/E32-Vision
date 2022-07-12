FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install apache2 -y
RUN apt-get install curl -y
RUN apt-get install apache2-utils -y
RUN apt-get clean
COPY . .
ADD start.sh /
RUN chmod +x /start.sh
EXPOSE 80
CMD [ "/start.sh"]