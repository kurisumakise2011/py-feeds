FROM python:3.6.7
WORKDIR /code

# I know that it's pain, but I'm really need this localtunnel
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

RUN nohup lt --port 8080 --subdomain pyfeeds > /dev/null &
ENTRYPOINT python app/main.py -c properties.yaml