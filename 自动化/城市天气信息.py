import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import Series, DataFrame
import datetime

# 城市以及天气日期
city = {'郸城': 'dancheng'}

# 模拟浏览器请求配置信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
url = f'https://lishi.tianqi.com/{city["郸城"]}/202208.html'

# 获取请求内容
resp = requests.request("GET", url, headers=headers)
resp.encoding = 'utf-8'
soup = bs(resp.text, 'html.parser')
data_all = []

# 过滤出天气信息
tian_three = soup.find("div", {"class": "tian_three"})
lishitable_content = tian_three.find_all("li")

# 循环抽取出每天的天气数据
# 格式化数据
for i in lishitable_content:
    lishi_div = i.find_all("div")
    data = []
    for j in lishi_div:
        data.append(j.text)
    data_all.append(data)
    weather = pd.DataFrame(data_all)
    weather.columns = ["当日信息", "最高气温", "最低气温", "天气", "风向信息"]
    weather_shape = weather.shape
    weather['当日信息'].apply(str)
    result = DataFrame(weather['当日信息'].apply(lambda x: Series(str(x).split(' '))))
    result = result.loc[:, 0:1]
    result.columns = ['日期', '星期']
    weather['风向信息'].apply(str)
    result1 = DataFrame(weather['风向信息'].apply(lambda x: Series(str(x).split(' '))))
    result1 = result1.loc[:, 0:1]
    result1.columns = ['风向', '级数']
    weather = weather.drop(columns='当日信息')
    weather = weather.drop(columns='风向信息')
    weather.insert(loc=0, column='日期', value=result['日期'])
    weather.insert(loc=1, column='星期', value=result['星期'])
    weather.insert(loc=5, column='风向', value=result1['风向'])
    weather.insert(loc=6, column='级数', value=result1['级数'])

weather.to_csv(f"{city.get('郸城')}的天气.csv", encoding="utf_8")
