import time
import paho.mqtt.client as paho
from paho import mqtt


request_topic = "ip_address_request"
response_topic = "ip_address_response"
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe(response_topic)
        client.publish(request_topic,"request_ip")
    else:
        print("Failed to connect, return code: " + str(rc))





        
        
def on_message(client, userdata, msg):
    print("Received IP address:", msg.payload.decode())


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("stephanie1", "12345678tT")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("0c8e979e14d842cabf744cca3da9217d.s2.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility

client.on_message = on_message


# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("ip", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("ip", payload="192.168.100.43", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()