import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import re
def tianqi_resp(url_bool, city_re):
    # 模拟浏览器请求配置信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    # 城市以及天气日期
    city = {'郸城': 'dancheng', '天津滨海新区': 'binhaixinqu', '上海浦东新区': 'pudong'}

    # 获取当前时间
    now = datetime.now()
    # 将年份和月份合并为一个字符串
    year_month = str(now.year) + str(now.month).zfill(2)  # 使用zfill(2)将月份转换为两位数，例如9月份变为09

    # 未来七天天气信息
    url_fut = f'https://www.tianqi.com/{city[city_re]}/7/'
    # 当月历史天气信息
    url_his = f'https://lishi.tianqi.com/{city[city_re]}/{year_month}.html'

    # 获取天气内容
    if url_bool == 'his':
        resp = requests.request("GET", url_his, headers=headers)
    else:
        resp = requests.request("GET", url_fut, headers=headers)

    resp.encoding = 'utf-8'
    soup = bs(resp.text, 'html.parser')
    parse(soup, city_re, url_bool)

def parse(soup, city_re, url_bool):
    data_all = []
    # 过滤出天气信息
    # 历史天气信息处理
    if url_bool == 'his':
        tian_three = soup.find("div", {"class": "tian_three"})
        lishitable_content = tian_three.find_all("li")

        # 循环过滤出每天的天气数据
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

    # 未来七天天气信息
    else:
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
            var_temperature_min, var_temperature_max = map(int, re.findall(r'\d+', var_temperature))

            # 风向
            # wind_direction = [wind_direction.text for wind_direction in i.find_all("div", {"class": "weaul_s"})][1]
            # print(wind_direction)

            data = []
            data.extend([var_data, var_week, var_temperature_max, var_temperature_min, var_weather])
            data_all.append(data)

    weather.to_csv(f"{city_re}天气.csv", encoding="utf_8")


if __name__ == '__main__':
    tianqi_resp('fut', '上海浦东新区')
