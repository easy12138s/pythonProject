# 发送请求模块
import requests
# 解析html模块
from lxml import etree
import re

# 发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
# 访问英雄主页
hero_url = 'https://pvp.qq.com/web201605/herodetail/548.shtml'
hero_resp = requests.get(hero_url, headers=headers)
hero_resp.encoding = 'gbk'
ehtml = etree.HTML(hero_resp.text)
# 筛选有多少
ehtml_xpa = ehtml.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
names = [ehtml_xpa[0:ehtml_xpa.index('&')] for name in ehtml_xpa.split('|')]



# 接收服务器响应的图片


# 保存接收的图片
