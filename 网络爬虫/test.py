import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}


response = requests.get('https://www.gamer520.com/go/?post_id=66068', headers=headers)

print(response.text)




