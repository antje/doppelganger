#!/bin/bash -e

docker build -t pipelineai/doppleganger:1.0.0 .
docker push pipelineai/doppleganger:1.0.0

kubectl create -f doppleganger-train.yaml

