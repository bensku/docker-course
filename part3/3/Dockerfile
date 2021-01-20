FROM alpine

RUN apk add --no-cache bash docker-cli git
WORKDIR /builder
COPY build.sh .

ENTRYPOINT [ "bash", "build.sh" ]