import csv
import requests
import re
import time


def main(page):
    url = f'https://tieba.baidu.com/p/8465843604?pn={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    html = resp.text
    print(html)

if __name__ == '__main__':
    with open('../01.csv', 'a', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(('评论用户', '评论时间', '评论内容'))
        for page in range(1, 8):  # 爬取前7页的内容
            main(page)
            time.sleep(2)