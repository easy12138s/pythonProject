import json
import requests
from lxml import etree, html

cookies = {
    'cao_notice_cookie': '1',
    'PHPSESSID': 'p47ljje7vl0d8eg54rkegiieq5',
}

headers = {
    'authority': 'www.gamer520.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'cao_notice_cookie=1; PHPSESSID=p47ljje7vl0d8eg54rkegiieq5',
    'origin': 'https://www.gamer520.com',
    'referer': 'https://www.gamer520.com/29217.html',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'user_down_ajax',
    'post_id': '29217',
}

response = requests.post('https://www.gamer520.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
data = json.loads(response.text)
