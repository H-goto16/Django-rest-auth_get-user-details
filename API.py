import json
import requests
import time

header = {"Authorization": "Token 1546b71af7249430ec6bfe69506d144459a21034"}

response = requests.get(
    "http://localhost:8000/rest-auth/user/", headers=header)
print(response)
print(json.loads(response.text))
