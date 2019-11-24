FROM node:12.2.0
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
RUN npm install
RUN npm install -g localtunnel
COPY . /app
CMD lt --port 4200 --subdomain fepyfeeds && ng serve --open --host 0.0.0.0 --port 4200 --disable-host-check
