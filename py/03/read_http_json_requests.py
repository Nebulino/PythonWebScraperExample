import json

import requests

planets_request = requests.get("http://localhost:8080/planets.json")
print(json.loads(planets_request.text))
