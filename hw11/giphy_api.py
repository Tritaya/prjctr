# search a word, return links to results
# python giphy_api.py

import requests

token = 'JLf7ZCjWQ2sDvYwXk2l6Hpvp1YwLsF8t'
end = 'https://api.giphy.com/v1/gifs/search'

# https://api.giphy.com/v1/gifs/search?api_key=JLf7ZCjWQ2sDvYwXk2l6Hpvp1YwLsF8t&q=cats&limit=25&offset=0&rating=g&lang=en

q = input('Enter something to search: ')

params = {
    'api_key': token,
    'q': q,
    'limit': 5,
    'offset': 0,
    # 'rating': 'g',
    # 'lang': 'en'
}

resp = requests.get(end, params=params)
obj = resp.json()

# if resp.ok:
    # print(resp.json())
print(resp.url)

for item in obj['data']:
    print(item['bitly_gif_url']
)