

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "al6gx5th5v6jo-ats.iot.eu-west-1.amazonaws.com"
CLIENT_ID = "RaspberryPi1"
PATH_TO_CERT = "/home/pi/certs/device.pem.crt"
PATH_TO_KEY = "/home/pi/certs/private.pem.key"
PATH_TO_ROOT = "/home/pi/certs/Amazon-root-CA-1.pem"
TOPIC = "test/mfs"
RANGE = 20

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=ENDPOINT,
            cert_filepath=PATH_TO_CERT,
            pri_key_filepath=PATH_TO_KEY,
            client_bootstrap=client_bootstrap,
            ca_filepath=PATH_TO_ROOT,
            client_id=CLIENT_ID,
            clean_session=False,
            keep_alive_secs=6
            )
print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")
# Publish message to server desired number of times.

def writeremote(timestamp, readings):
    print('Begin Publish')
    payload = { "state":
        { "timestamp": timestamp,
          "reported":[
              {"sensor": "1",
               "temp": str(readings[0])
               },
              {"sensor": "2",
               "temp": str(readings[1])
               }]
          }
    }

    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(payload), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + json.dumps(payload) + "' to the topic: " + "'test/testing'")
    t.sleep(0.1)
    print('Publish End')

def disconnect():
    print('Disconnecting')
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print('Disconnected')