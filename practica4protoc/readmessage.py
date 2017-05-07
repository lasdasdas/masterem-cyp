#! /usr/bin/python3

import datalog_pb2
import sys
import paho.mqtt.client as mqtt

# Iterates though all people in the DataLog and prints info about them.
def ListPeople(data_log):
  for station in data_log.station:
    print ("ZIP code: ", station.postal)
    print (" Town name:", station.town)
    if station.clouds!=None:
      print ("Cloud status :", station.clouds)

    for data_entry in station.data:
      if data_entry.cat == 0:
        print ("Humididylevel :")
      elif data_entry.cat == 1:
        print ("Temeprature level:")
      elif data_entry.cat == 2:
        print ("Light level :")
      print (data_entry.cat)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/etsidi/#")
def on_message(client1, userdata, message):
    print("message received  " )
    data_log.ParseFromString(message.payload)
    ListPeople(data_log)

# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.


data_log = datalog_pb2.DataLog()
#client connect
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
