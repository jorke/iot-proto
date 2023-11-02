# IoT Core protobuf example

## Generate filedescriptor from protobufs

`protoc --descriptor_set_out=filedescriptor.desc --proto_path=. --include_imports Measurements.proto`


## Example test sending telemetry data

`AWS_REGION=ap-southeast-2 IOT_ENDPOINT=xxx-ats.iot.ap-southeast-2.amazonaws.com python3 test_send.py`
