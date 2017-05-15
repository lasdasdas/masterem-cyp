#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import time

# URL proporcionada por Carriots para enviar datos
api_url = "http://api.carriots.com/streams"

# ID de nuestro dispositivo (de la forma algo@user.user)
device = "defaultDevice@thunderbird1.thunderbird1"

# La APIKEY de cada uno
api_key = "2cfb12bf7c883ef81a59a324a4cae6687b816427d259641f1d7100e4907c03ee"

# El tipo de contenido que vamos a mandar, en nuestro caso JSON
content_type = "application/json"     

# La fecha/hora en formato timestamp
timestamp = int(time.time())

header = {"carriots.apikey": api_key}

req = urllib.request.Request(api_url,None,header)
#req.get_method = lambda: "GET"
f = urllib.request.urlopen(req)

data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))

