#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
import json
import sys
import time
import urllib.request, urllib.parse
import json



api_url = sys.argv[1]
req = urllib.request.Request(api_url)
f = urllib.request.urlopen(req)

# Imprimimos el resultado
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
for element in data["_items"]:
    print(element["_etag"])
    print(element["_id"])

if len(data["_items"])>0:
    req = urllib.request.Request(api_url+str(data["_items"][0]["_id"]))
    req.add_header('If-Match',data["_items"][0]["_etag"])
    req.add_header('Content-type','application/json; charset=utf-8')
    req.get_method = lambda: "DELETE"
    f = urllib.request.urlopen(req)
    print(f.read().decode('utf-8'))
