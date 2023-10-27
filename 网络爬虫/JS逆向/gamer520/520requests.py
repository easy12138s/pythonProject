# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 520requests.py
    @time: 2023/10/27 10:40
"""
import pandas as pd
import requests
from lxml import etree, html

def requests_gamer520(page):
    weather_play = pd.DataFrame(None, columns=["一级下载网址", "游戏名"])
    for i in range(1, page+1, 1):
        page = '' if i == 1 else f'/page/{i}'
        url = f'https://www.gamer520.com/pcgame{page}'

        cookies = {
            'cao_notice_cookie': '1',
            'PHPSESSID': 'p47ljje7vl0d8eg54rkegiieq5',
        }

        headers = {
            'authority': 'www.gamer520.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'cao_notice_cookie=1; PHPSESSID=p47ljje7vl0d8eg54rkegiieq5',
            'referer': url,
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        }

        response = requests.get(url, cookies=cookies, headers=headers)

        data = response.text
        data_xp = etree.HTML(data)
        list_play = data_xp.xpath('//h2[@class="entry-title"]/a/@href')
        list_play2 = data_xp.xpath('//h2[@class="entry-title"]/a/text()')
        # str_play = html.tostring(list_play[0], encoding='utf-8').decode('utf-8')

        data_list = [list_play, list_play2]
        weather_data = pd.DataFrame(data_list, index=["一级下载网址", "游戏名"]).T
        weather_play = weather_play._append(weather_data)
    return weather_play.reset_index(drop=True)

if __name__ == '__main__':
    data = requests_gamer520(50)
    data.to_csv('games.csv', encoding='utf-8')
    data.to_excel('games.xlsx', sheet_name="一级游戏目录",index = False,na_rep = 0,inf_rep = 0)