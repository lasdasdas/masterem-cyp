import time
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    m="Connected flags: " + str(flags) + " result code: " + str(rc) + " client1_id: " + str(client)
    print(m)
#broker_address="192.168.1.184" # Use the Raspberry Pi IP address

broker_address="iot.eclipse.org"
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_address, 1883, 60)
client.loop_start()    #start the loop
while(True):
        msg2=json.dumps({"usuario":"david" , "time":time.time()})
        time.sleep(5)
        client.publish("/etsidi/val",msg2) # Publicamos
client.disconnect()
client.loop_stop()
