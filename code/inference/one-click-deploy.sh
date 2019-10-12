#!/bin/bash -e

docker build -t pipelineai/doppelganger-similar:1.0.0 .
docker push pipelineai/doppelganger-similar:1.0.0

kubectl create -f similar-deploy.yaml
