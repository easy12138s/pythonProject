import json
from urllib.request import urlopen

import requests


def getCountry(ipAddress):
    response = requests.get("https://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    print(response)
    responseJson = json.loads(response)
    return responseJson.get("country_code")


print(getCountry("50.78.253.58"))
