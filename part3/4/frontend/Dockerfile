FROM ubuntu
WORKDIR /app

RUN apt-get -qq update && apt-get -qq install curl && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash && \
    apt-get -qq install nodejs && \
    apt-get purge -qq --auto-remove curl && \
    rm -rf /var/lib/apt/lists/*

COPY --chown=5050:5050 frontend-example-docker .
RUN npm install && chown -R 5050:5050 .

EXPOSE 5000
USER 5050:5050
ENV API_URL=http://localhost:8000
CMD npm start
