FROM ubuntu
WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get -qq install nodejs

COPY backend-example-docker .
RUN npm install

EXPOSE 8000
CMD npm start
