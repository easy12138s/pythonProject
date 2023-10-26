# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: WebTab.py
    @time: 2023/10/26 16:57
"""
import json

import requests

# 资讯平台
hot_web = ['toutiao', 'douyin', 'bilibili', 'wechat', 'zhihu', 'baidu']

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'If-None-Match': 'W/"cd6-zCTP+nSVPU3RQyCYJsME4Afz2BE"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'i-app': 'hitab',
    'i-branch': 'zh',
    'i-lang': 'zh-CN',
    'i-platform': 'chrome',
    'i-version': '1.3.6',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'type': hot_web[0],
}

response = requests.get('https://api.wetab.link/api/hotsearch/list', params=params, headers=headers)

data = json.loads(response.text)
data_list = data['data']['list']

with open(f'{hot_web[0]}.txt', 'a', encoding='UTF-8') as f:
    for list_item in data_list:
        hot_data = list_item['title'] + '--' + list_item['url']
        f.write(hot_data)
        f.write('\n')
