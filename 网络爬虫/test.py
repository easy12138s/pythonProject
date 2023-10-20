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
cookies = {
    'SINAGLOBAL': '115445762559.89148.1689583983224',
    'UOR': ',,login.sina.com.cn',
    'ULV': '1696819297273:7:1:1:8610694135791.372.1696819297270:1695880142641',
    'XSRF-TOKEN': 'Luj5hSiSEzoABcJkSIiCQqQS',
    'SUB': '_2AkMSbWd2f8NxqwFRmPAWzmjkboR0zwjEieKkMZatJRMxHRl-yT9kqnxctRB6Oe1JmZabPK7dAvgeriICelP2-rabFk6x',
    'SUBP': '0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh1uo6l4lX7LYJSG1YJ_DSB',
    'WBPSESS': 'eyDLPcU90tHVPRrsWrtAPvJJMu2507deQZmPTsltY-Q7xX8osLamqSwWS6xfm97GQlNeS32Cvm9NfUollja60WH5jDIrtOtdtFP3q-NdGQJIKe3s3BYm9iglI_p5PWUjdskEXS7L4we2Ad9frs9g-jga9TRY8sBgaTnJVJbIYiw=',
}

headers = {
    'authority': 'weibo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'client-version': 'v2.44.3',
    # 'cookie': 'SINAGLOBAL=115445762559.89148.1689583983224; UOR=,,login.sina.com.cn; ULV=1696819297273:7:1:1:8610694135791.372.1696819297270:1695880142641; XSRF-TOKEN=Luj5hSiSEzoABcJkSIiCQqQS; SUB=_2AkMSbWd2f8NxqwFRmPAWzmjkboR0zwjEieKkMZatJRMxHRl-yT9kqnxctRB6Oe1JmZabPK7dAvgeriICelP2-rabFk6x; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh1uo6l4lX7LYJSG1YJ_DSB; WBPSESS=eyDLPcU90tHVPRrsWrtAPvJJMu2507deQZmPTsltY-Q7xX8osLamqSwWS6xfm97GQlNeS32Cvm9NfUollja60WH5jDIrtOtdtFP3q-NdGQJIKe3s3BYm9iglI_p5PWUjdskEXS7L4we2Ad9frs9g-jga9TRY8sBgaTnJVJbIYiw=',
    'referer': 'https://weibo.com/newlogin?tabtype=search&gid=&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2023.10.19.2',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'Luj5hSiSEzoABcJkSIiCQqQS',
}

response = requests.get('https://weibo.com/ajax/side/hotSearch', cookies=cookies, headers=headers)
data = json.loads(response.text)
print(data['data'])