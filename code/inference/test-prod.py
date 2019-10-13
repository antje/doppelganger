curl http://<ip-address>/seldon/deployment/doppelganger-model/api/v0.1/predictions -d '{"data":{"ndarray":[[1]]}}' -H "Content-Type: application/json"
