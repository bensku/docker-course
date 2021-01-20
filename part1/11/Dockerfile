FROM ubuntu
WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get -qq install nodejs

COPY backend-example-docker .
RUN npm install

EXPOSE 8000
ENV FRONT_URL=http://localhost:5000
CMD npm start
