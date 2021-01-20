FROM node:12-alpine
WORKDIR /app

COPY --chown=5050:5050 frontend-example-docker .
RUN npm install && chown -R 5050:5050 .

EXPOSE 5000
USER 5050:5050
ENV API_URL=http://localhost:8000
CMD npm start
