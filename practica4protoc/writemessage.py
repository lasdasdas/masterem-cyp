#! /usr/bin/python3

import datalog_pb2
import sys
import paho.mqtt.client as mqtt

# This function fills in a Station message based on user input.
def PromptForData(station):
  station.postal = int(input("Enter ZIP code: "))
  station.town = input("Enter town:")
  clouds = input("Enter cloud sitiuation(blank for none): ")
  if clouds != "":
      station.clouds = clouds
  while True:
    number = input("Enter s sensor sensor data (or leave blank to finish): ")
    if number == "":
      break
    data_capture = station.data.add()
    data_capture.number = float(number)
    type1 = input("Is this humidity(0), temeprature(1), or light level(2)? ")
    if type1 == "0":
      data_capture.cat = int(1)
    elif type1 == "1":
      data_capture.cat =int(2)
    elif type1 == "2":
      data_capture.cat =int(3)
    else:
      print ("Unknown phone type; leaving as default value.")
      print(type1)

def on_connect(client, userdata, flags, rc):
    m="Connected flags: " + str(flags) + " result code: " + str(rc) + " client1_id: " + str(client)
    print(m)

def main():
    if len(sys.argv) != 2:
      print ("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
      sys.exit(-1)

    datalog= datalog_pb2.DataLog()

    # Read the existing address book.
    try:
      f = open(sys.argv[1], "rb")
      datalog.ParseFromString(f.read())
      f.close()
    except IOError:
      print (sys.argv[1] + ": Could not open file.  Creating a new one.")

    # Add an address.
    PromptForData(datalog.station.add())

    #Connecting mqtt
    broker_address="iot.eclipse.org"
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(broker_address, 1883, 60)
    client.loop_start()    #start
    client.publish("/etsidi/val",datalog.SerializeToString()) # Publicamos
    print("published")
    client.disconnect()
    client.loop_stop()

    # Write the new address book back to disk.
    f = open(sys.argv[1], "wb")
    f.write(datalog.SerializeToString())
    f.close()
if __name__ == '__main__':
    main()
