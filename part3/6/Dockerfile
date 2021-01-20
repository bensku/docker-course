FROM node:12-alpine as builder
WORKDIR /app

COPY --chown=5050:5050 frontend-example-docker .
RUN npm install && npm run build && chown -R 5050:5050 .

FROM node:12-alpine
WORKDIR /app
COPY --from=builder /app/package.json package.json
COPY --from=builder /app/node_modules node_modules
COPY --from=builder /app/dist dist

EXPOSE 5000
USER 5050:5050
ENV API_URL=http://localhost:8000
CMD npx serve -s -l 5000 dist
