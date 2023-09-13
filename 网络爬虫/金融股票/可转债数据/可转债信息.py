import requests
from bs4 import BeautifulSoup as bs, Comment
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import re
import warnings

warnings.filterwarnings('ignore')

# 模拟浏览器请求配置信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76'
}
params = {
    'type': '1',
    'order_by': '1m',
    'size': '20',
    'page': '3',
}
url = 'https://www.jisilu.cn/web/data/'

resp = requests.request("GET", url, headers=headers, params=params)
resp.encoding = 'utf-8'

soup = bs(resp.text, 'html.parser')

df = soup.find("div", {"class": "dataview-body"})

print(soup)
