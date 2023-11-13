# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2418087868@qq.com
    @software: PyCharm
    @file: 520requests.py
    @time: 2023/10/27 10:40
"""
import re
import pandas as pd
import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}


def gamer520_1(page):
    weather_play = pd.DataFrame(None, columns=["一级下载网址", "游戏名"])
    for i in range(1, page + 1, 1):
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

        data1 = response.text
        data_xp = etree.HTML(data1)
        list_play = data_xp.xpath('//h2[@class="entry-title"]/a/@href')
        list_play2 = data_xp.xpath('//h2[@class="entry-title"]/a/text()')
        # str_play = html.tostring(list_play[0], encoding='utf-8').decode('utf-8')

        data_list = [list_play, list_play2]
        weather_data = pd.DataFrame(data_list, index=["一级下载网址", "游戏名"]).T
        weather_play = weather_play._append(weather_data)

    return weather_play.reset_index(drop=True)


def gamer520_2(page):
    weather_df = gamer520_1(page)
    weather_url = weather_df["一级下载网址"]
    weather_name = weather_df["游戏名"].str
    id_1 = weather_url.str.split('/')
    id_list = [i[3].replace('.html', '') for i in id_1]
    url_list = []
    for id_3 in id_list:
        game_id = id_3
        response = requests.post(f'https://www.gamer520.com/go?post_id={game_id}', headers=headers)
        data_js = response.text  # <script type='text/javascript'>window.location='https://xxxxx528.com/19886.html';setTimeout(function(){window.close()},5000)</script>
        data_url = re.findall(r'location=\'(.*)\';', data_js)[0]
        url_list.append(data_url)

    weather_df['二级下载网址'] = url_list
    return url_list, weather_df


def gamer520_3(page):
    url_list, weather_df = gamer520_2(page)
    data_link = []
    for url in url_list:
        response = requests.post(url, headers=headers)
        data = etree.HTML(response.text)
        data_s = data.xpath('//meta[@name="description"]/@content')
        data_link.append(data_s)
    weather_df['三级下载地址'] = data_link
    weather_df.to_csv('games.csv')


def main(page):
    gamer520_3(page)
    weather_df = pd.read_csv('games.csv')

    weather_df['三级下载地址'] = (weather_df['三级下载地址'].str.replace('\'', '').str.replace(': ', ':')
                                  .str.replace('点我  ', '').str.replace(' [立即下载]', '').str.replace('[',
                                                                                                        '').str.replace(
        ']', '')
                                  .str.split('  '))

    data_list = weather_df['三级下载地址'].values.tolist()
    weather_df['三级下载地址'] = data_list[0][0]
    weather_df['提取码'] = data_list[0][1]
    weather_df['解压密码'] = data_list[0][-1]
    weather_df1 = weather_df.drop(columns=['Unnamed: 0', '一级下载网址', '二级下载网址'])
    weather_df1.to_csv('games.csv', index=False)
    weather_df1.to_excel('games.xlsx', index=False)


if __name__ == '__main__':
    main(10)
