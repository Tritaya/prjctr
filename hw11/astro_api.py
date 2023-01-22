# python astro_api.py
import requests
url = 'http://api.open-notify.org/astros.json'

try:
    resp = requests.get(url)
except requests.exceptions.RequestException as e:
    print(repr(e))

data = resp.json()

print(resp.status_code)

ls = data['people']

for record in ls:
    match record:
        case {'name': name}:
            print(name)

