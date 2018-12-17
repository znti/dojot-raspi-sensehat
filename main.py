import paho.mqtt.client as mqtt
import json
import time

#
# Properties definition
tenant_name = "admin"
device_id = "a6559f"

#
# Internal definitions setup
client_id = "{}:{}".format(tenant_name, device_id)
topic_to_publish = "/{}/{}/attrs".format(tenant_name, device_id)

#
# MQTT Client setup and connection
client = mqtt.Client(client_id)

print("Connecting to mqtt broker")
client.connect(host='localhost', port=1883)
client.loop_start()

#
# Execution loop
while True:
    message = {
        "temperature" : 35.11,
        "pressure": 773.29,
        "humidity": 66.23
    }
    print("Publishing", message, 'to topic', topic_to_publish)
    client.publish(topic_to_publish, json.dumps(message))
    time.sleep(4)
