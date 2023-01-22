# python weather_api.py

import requests
import json
from pprint import pprint

token = '716b2de347d59aa615cc11568c41f6d2'
url = 'https://api.openweathermap.org/data/2.5/weather'

# просто вирішив так спробувати, в реальному житті не буду
class P:
    pass

p= P()

q = input('What city are you looking the weather for? ')

p.q = q
p.appid = token

params = p.__dict__

# helper function, finds a node (credit to Raymond Hettinger)
'''
path_to('London', data)
'''
def path_to(target, node) -> str:
    class Var:
        pass
    var = Var()
    var.target = target
    match node:
        case var.target:
            return f'--> {target!r}'
        case list():
            for i, subnode in enumerate(node):
                if (path := path_to(target, subnode)):
                    return f'[{i}]' + path
        case dict():
            for key, subnode in node.items():
                if (path := path_to(target, subnode)):
                    return f'[{key!r}]' + path
    return ''


try:
    resp = requests.get(url, params=params)
    print(resp.url)
    # print(resp.status_code)
    resp.raise_for_status()
except requests.exceptions.RequestException as e:
    # print (repr(e))
    print("We don't have data for this location")
    exit()


data = resp.json()
# pprint(data)


# with open('del.json', 'w') as f:
#     (json.dump(data, f))
    # f.write(json.dump(data, f))

# print(path_to(82, data))
weather = data['weather'][0]['description']
humidity = data['main']['humidity']
print('The data for:', q)
print('Weather:', weather)
print('Humidity:', humidity)