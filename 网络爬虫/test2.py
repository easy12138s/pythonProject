# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: test2.py
    @time: 2023/10/27 14:13
"""
import requests

cookies = {
    'cao_notice_cookie': '1',
    'PHPSESSID': 'r63vqsa98cuoi8u4mbeu46opgo',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wp-postpass_064a239b4db34ca309bbd53324e192c5': '%24P%24Balkru.uXhTiX1oPsAI8WNdI6IVmn10',
}

headers = {
    'authority': 'dow.gamers520.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'cao_notice_cookie=1; PHPSESSID=r63vqsa98cuoi8u4mbeu46opgo; wordpress_test_cookie=WP%20Cookie%20check; wp-postpass_064a239b4db34ca309bbd53324e192c5=%24P%24Balkru.uXhTiX1oPsAI8WNdI6IVmn10',
    'referer': 'https://www.gamer520.com/',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

response = requests.get('https://dow.gamers520.com/27779.html', cookies=cookies, headers=headers)
print(response.text)