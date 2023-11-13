import json

import requests

cookies = {
    'PHPSESSID': 's8oits6sq4poiu85f1q8slsa21',
    'cao_notice_cookie': '1',
}

headers = {
    'authority': 'www.gamer520.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=s8oits6sq4poiu85f1q8slsa21; cao_notice_cookie=1',
    'origin': 'https://www.gamer520.com',
    'referer': 'https://www.gamer520.com/51800.html',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'action': 'user_down_ajax',
    'post_id': '51800',
}

response = requests.post('https://www.gamer520.com/wp-admin/admin-ajax.php', headers=headers, data=data)
data_url = json.loads(response.text)['msg']
print(data_url)
