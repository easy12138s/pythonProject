# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2382019442@qq.com
    @software: PyCharm
    @file: 有道翻译.py
    @time: 2023/10/17 10:20
"""
import time
import requests

e = int(time.time()*1000)
d = 'fanyideskweb'
u = 'wifi'
t = 'fsdsogkndfoka'
sign_md5 = f'client=${d}&mysticTime=${e}&product=${u}&key=${t}'

cookies = {
    'P_INFO': 'null',
    'OUTFOX_SEARCH_USER_ID': '-997082143@10.110.96.153',
    'OUTFOX_SEARCH_USER_ID_NCOO': '1926107383.121204',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'P_INFO=null; OUTFOX_SEARCH_USER_ID=-997082143@10.110.96.153; OUTFOX_SEARCH_USER_ID_NCOO=1926107383.121204',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'i': '你好',
    'from': 'auto',
    'to': '',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': '1bf39476f9ed69ca521d3117d8a88b83',
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': '1697522907135',
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
print(response.text)
