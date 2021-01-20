FROM node:12-alpine
WORKDIR /app

COPY backend-example-docker .
RUN npm install

EXPOSE 8000
ENV FRONT_URL=http://localhost:5000
USER 5050:5050
CMD npm start
