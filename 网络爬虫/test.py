# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2382019442@qq.com
    @software: PyCharm
    @file: test.py
    @time: 2023/10/19 17:15
"""
import json

import requests

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVpZCI6IjY0YmEyZDk4OTVkNzIxNjVlNjRhYzkwOSIsInZlcnNpb24iOjAsImJyYW5jaCI6InpoIn0sImlhdCI6MTY5NzY5ODUyNCwiZXhwIjoxNjk3ODcxMzI0fQ.eB9cYq9Z5sXki8_iT7Lqc1x0ADcRJUMBeZ8ClsuISjo',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'chrome-extension://aikflfpejipbpjdlfabpgclhblkpaafo',
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

json_data = {
    'prompt': '你好',
    'assistantId': '',
    'model': '650e52e9c4bcb4a52791b599',
}

response = requests.post('https://wetabchat.haohuola.com/api/chat/conversation-v2', headers=headers, json=json_data)
date = response.text

date_list = list(date.split('_e79218965e_'))
print(date_list)
