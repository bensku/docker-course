FROM ubuntu
WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get -qq install nodejs

COPY frontend-example-docker .
RUN npm install

EXPOSE 5000
ENV API_URL=http://localhost:8000
CMD npm start
