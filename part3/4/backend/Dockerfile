FROM ubuntu
WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash && \
    apt-get -qq install nodejs && \
    apt-get purge -qq --auto-remove curl && \
    rm -rf /var/lib/apt/lists/*

COPY backend-example-docker .
RUN npm install

EXPOSE 8000
ENV FRONT_URL=http://localhost:5000
USER 5050:5050
CMD npm start
