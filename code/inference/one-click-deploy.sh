#!/bin/bash -e

docker build -t antjebarth/doppelganger-predict:1.0.0 .
docker push antjebarth/doppelganger-predict:1.0.0

kubectl create -f similar-deploy.yaml
