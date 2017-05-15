#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time

# URL proporcionada por Carriots para enviar datos
api_url = "http://api.carriots.com/streams/"

# ID de nuestro dispositivo (de la forma algo@user.user)
device = "defaultDevice@thunderbird1.thunderbird1"

# La APIKEY de cada uno
api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"
content_type = "application/json"



headers = {
'User-Agent': 'Raspberry-Carriots',
'Carriots.apikey': api_key,
}

req = urllib.request.Request(api_url, headers=headers)

data=json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
print(data["result"][0]["id_developer"])
print(json.dumps(data,indent=4,sort_keys=True))

api_url = api_url+str(data["result"][0]["id_developer"])+"/"
print(api_url+str(data["result"][0]["id_developer"]))

header = {"User-Agent": "raspberrycarriots", "Content-Type": content_type,"carriots.apikey": api_key}

req = urllib.request.Request(api_url)
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))


req.get_method = lambda: "DELETE"
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
