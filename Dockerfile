FROM python:3.6.5
WORKDIR /code

RUN apt-get update
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y npm

ENV PYTHONPATH='.'
ADD app app
ADD setup.py setup.py
ADD config/properties_docker.yaml properties.yaml

RUN mkdir log
RUN pip install .

RUN npm install -g localtunnel

CMD lt --port 8080 --subdomain pyfeeds && python app/main.py -c properties.yaml