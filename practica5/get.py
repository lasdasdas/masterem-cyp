#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import sys
import time
import urllib.request, urllib.parse
import json

# Leemos la URL de la line de comandos,ej.: python3 ./demo-get.py http://127.0.0.1:5000/medida
api_url = sys.argv[1]

# Creamos un request con la URL
req = urllib.request.Request(api_url)

# Normalmente es necesario indicar el método que vamos a isar: GET, POST, DELETE, etc.
#req.get_method = lambda: "DELETE"

# Realizamos la petición
f = urllib.request.urlopen(req)

# Imprimimos el resultado
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
for element in data["_items"]:
    print(element["_etag"])
    print(element["_id"])
