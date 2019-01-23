from sense_emu import SenseHat
import paho.mqtt.client as mqtt
import json
import time
import ssl

#
# Properties definition
tenant_name = "admin"
device_id = "36fc0a"
certs_dir= "/etc/ssl/certs"

#
# Internal definitions setup
client_id = "{}:{}".format(tenant_name, device_id)

ca_cert="/{}/IOTmidCA.crt".format(certs_dir)
cert_file="/{}/{}.crt".format(certs_dir, device_id)
key_file="/{}/{}.key".format(certs_dir, device_id)

topic_to_publish = "/{}/{}/attrs".format(tenant_name, device_id)
topic_to_subscribe = "/{}/{}/config".format(tenant_name, device_id)

def on_message(client, userdata, message):
    decoded_message = json.loads(message.payload.decode())
    message_text = decoded_message['display']
    print("Received", decoded_message)
    sense.clear()
    if message_text == "high":
        sense.show_message("HOT")
    elif message_text == "low":
        sense.show_message("COLD")


#
# MQTT Client setup and connection
client = mqtt.Client(client_id)
client.tls_set(ca_certs=ca_cert, certfile=cert_file, keyfile=key_file, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2)
client.on_message = on_message

print("Connecting to mqtt broker")
client.connect(host='localhost', port=8883)
client.loop_start()

print("Subscribing to topic", topic_to_subscribe)
client.subscribe(topic_to_subscribe)

#
# Raspberry Pi's Sensor initialization
print("Initializing SenseHat emulator")
sense = SenseHat()

#
# Execution loop
while True:
    message = {
        "temperature" : sense.temperature,
        "pressure": sense.pressure,
        "humidity": sense.humidity
    }
    print("Publishing", message, 'to topic', topic_to_publish)
    client.publish(topic_to_publish, json.dumps(message))
    time.sleep(4)

