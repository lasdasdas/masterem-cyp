import urllib.request, urllib.parse
import json
data  = {"tipo": "temp",
      "identificador": "t002",
      "ciudad": "madrid",
      "fecha": "Mon, 09 May 2016 21:29:13 GMT",
      "valor": 30}
headers = {'Content-type': 'application/json; charset=utf-8'}


data = json.dumps(data).encode('ascii')
req = urllib.request.Request('http://0.0.0.0:5000/medida',data)
req.add_header('Content-type','application/json; charset=utf-8')


f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

