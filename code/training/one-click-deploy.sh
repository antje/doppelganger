#!/bin/bash -e

docker build -t pipelineai/doppelganger:1.0.0 .
docker push pipelineai/doppelganger:1.0.0

kubectl create -f doppelganger-train.yaml

