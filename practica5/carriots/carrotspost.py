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

# Los datos que vamos a subir. Podemos seguir el mismo schema que antes o utilizar uno cualquie-ra
mydata = {'tipo': 'temp',
      'identificador': 't003',
      'ciudad': 'Segovia',
      'fecha': 'hoy',
      'valor': 30}

# Los parámetros requeridos por Carrios: unos obligatorios y otros opcionales
params = {"protocol": "v2",
              "device": device,
              "at": timestamp,
              "data": mydata}
binary_data = json.dumps(params).encode('ascii')

# La cabecera, imprescindible el APIKEY
header = {"User-Agent": "raspberrycarriots", "Content-Type": content_type,"carriots.apikey": api_key}

req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
