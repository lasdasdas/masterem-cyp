import paho.mqtt.client as mqtt  #import the client1ç
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
	for a in "hola en letras!":
		client.publish("/etsidi/val",a) # Publicamos
client.disconnect()
client.loop_stop()

