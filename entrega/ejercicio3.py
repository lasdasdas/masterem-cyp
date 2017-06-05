#!/usr/bin/python3
import reed
import temperature
import sys
import http.client
import urllib.request
import urllib.parse
import json
import time
import RPi.GPIO as GPIO
PIN_BUTTON1=13
PIN_BUTTON2=26

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def getStatesButtons():
    stateButton1 = GPIO.input(PIN_BUTTON1)
    if stateButton1 == False:
        print('Button 1 Pressed')
        api_url = "http://api.carriots.com/streams"
        device = "defaultDevice@thunderbird1.thunderbird1"
        api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"
        content_type = "application/json"

        mydata = {'tipo': 'temp',
        'identificador': 'abcdef',
        'fecha':  int(time.time()),
        'valor': temperature.read_temp()}
        params = {"protocol": "v2",
              "device": device,
              "at": timestamp,
              "data": mydata}
        binary_data = json.dumps(params).encode('ascii')

        header = {"User-Agent": "raspberrycarriots", "Content-Type": content_type,"carriots.apikey": api_key}
        req = urllib.request.Request(api_url,binary_data,header)
        f = urllib.request.urlopen(req)
        print(f.read().decode('utf-8'))
        time.sleep(5)
    else:
        print('Button 1 Not Pressed')
    stateButton2 = GPIO.input(PIN_BUTTON2)
    if stateButton2 == False:
        print('Button 2 Pressed')
        api_url = "http://api.carriots.com/streams/"

        device = "defaultDevice@thunderbird1.thunderbird1"

        api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"
        content_type = "application/json"
        content_type = "application/json"

        api_url = "http://api.carriots.com/streams/"
        api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"
        content_type = "application/json"
        content_type = "application/json"



        headers  = {
'User-Agent': 'Raspberry-Carriots',
'Carriots.apikey': api_key,
        }

        req = urllib.request.Request(api_url, headers=headers)

        data=json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
        print(data["result"][0]["id_developer"])
        print(json.dumps(data,indent=4,sort_keys=True))

        api_url = api_url+str(data["result"][0]["id_developer"])+"/"
        print(api_url)
        params = {"protocol": "v2"}
        binary_data = json.dumps(params).encode('ascii')
        header = {"carriots.apikey": api_key}
        req = urllib.request.Request(api_url,binary_data,header)
        req.get_method = lambda: "DELETE"
        f = urllib.request.urlopen(req)
        print(f.read().decode('utf-8'))
        time.sleep(5)
    else:
        print("nopressed 2")



api_url = "http://api.carriots.com/streams"
device = "defaultDevice@thunderbird1.thunderbird1"
api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"
content_type = "application/json"
timestamp = int(time.time())
def main():
     while(True):
        getStatesButtons()
#Run main
if __name__ == "__main__":
    main()




