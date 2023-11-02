import sys
sys.path.insert(0, 'protobuf')

import boto3
from botocore.config import Config
from datetime import datetime
import os
from random import random
import time

from google.protobuf.json_format import MessageToJson
from protobuf.Measurements_pb2 import Measurement, Quality


AWS_REGION = os.environ['AWS_REGION'] or 'us-west-2'
IOT_ENDPOINT = os.environ['IOT_ENDPOINT']
TOPIC = 'test/all_telemetry'

config = Config(region_name=AWS_REGION)

c_iot_data = boto3.client('iot-data', config=config, endpoint_url='https://{}'.format(IOT_ENDPOINT))

while True:
    m = Measurement()
    q = Quality()

    q.validity = Quality.QUESTIONABLE
    m.type = Measurement.STRING
    m.name = "hello"
    m.quality.CopyFrom(q)
    m.time = int(datetime.now().strftime("%s")) * 1000 

    serialized = m.SerializeToString()
    
    try:
        res = c_iot_data.publish(topic=TOPIC, qos=1, payload=serialized)
        print(f"Published message {MessageToJson(m)} to AWS IoT")
        time.sleep(5)
    except KeyboardInterrupt:
      print("Exiting")
      break
    except Exception as e:
        print(e)
        break