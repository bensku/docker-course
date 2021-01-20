#!/bin/bash

HUB_NAME=$1
GIT_URL=$2

git clone "$GIT_URL" repo
docker build -t "$HUB_NAME" repo
docker login --username $HUB_USER --password $HUB_PASSWORD
docker push "$HUB_NAME"