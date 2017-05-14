import urllib.request, urllib.parse
import json



data = {"valor": 13}
headers = {'Content-type': 'application/json; charset=utf-8'}


data = json.dumps(data).encode('ascii')
req = urllib.request.Request('http://0.0.0.0:5000/medida/5918e8244b424c2260428a5d',data)
req.add_header('If-Match','a57c09fb120435692ad184431c330b938690d615')
req.add_header('Content-type','application/json; charset=utf-8')
req.get_method = lambda: "PATCH"
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

