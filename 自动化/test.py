import requests
from bs4 import BeautifulSoup as bs, Comment
import re
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime


def remove_html_comments(soup1):
    # 去除注释符号
    comment_tags = soup1.find_all(string=lambda text: isinstance(text, Comment))
    comment_contents = [comment.strip() for comment in comment_tags if comment.strip()]
    # for comment in comment_contents:
    #     print(comment)
    return soup1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

url_fut = f'https://www.tianqi.com/pudong/7/'
url_his = 'https://lishi.tianqi.com/anyuanqu/202308.html'
resp = requests.request("GET", url_fut, headers=headers)
resp.encoding = 'utf-8'

soup = bs(resp.text, 'html.parser')
tian_three = soup.find("ul", {"class": "weaul"}).find_all("li")
now = datetime.now()
data_all = []
for i in tian_three:
    # 日期
    var_data = i.find('div', class_='weaul_q').find('span', class_='fl').text
    var_data = str(now.year) + '-' + str(var_data)
    var_week = i.find('div', class_='weaul_q').find('span', class_='fr').text
    # 天气
    var_weather = i.find('div', class_='weaul_z').text
    # 温度
    var_temperature = [var_temperature.text for var_temperature in i.find_all("div", {"class": "weaul_z"})][1]
    var_temperature_min,  var_temperature_max = map(int, re.findall(r'\d+', var_temperature))

    # 风向
    # wind_direction = [wind_direction.text for wind_direction in i.find_all("div", {"class": "weaul_s"})][1]
    # print(wind_direction)

    data = []
    data.extend([var_data, var_week, var_temperature_max, var_temperature_min, var_weather])
    data_all.append(data)
