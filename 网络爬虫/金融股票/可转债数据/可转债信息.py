import json
import requests
import re
import warnings
from bs4 import BeautifulSoup as bs, Comment
warnings.filterwarnings('ignore')

# 模拟浏览器请求配置信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    'Referer': 'https://data.eastmoney.com/'
}
# 获取数据
# url = 'https://datacenter-web.eastmoney.com/api/data/v1/get?callback=jQuery112305445752770008432_1694676002292&sortColumns=PUBLIC_START_DATE&sortTypes=-1&pageSize=50&pageNumber=1&reportName=RPT_BOND_CB_LIST&columns=ALL&quoteColumns=f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE%2Cf235~10~SECURITY_CODE~TRANSFER_PRICE%2Cf236~10~SECURITY_CODE~TRANSFER_VALUE%2Cf2~10~SECURITY_CODE~CURRENT_BOND_PRICE%2Cf237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO%2Cf239~10~SECURITY_CODE~RESALE_TRIG_PRICE%2Cf240~10~SECURITY_CODE~REDEEM_TRIG_PRICE%2Cf23~01~CONVERT_STOCK_CODE~PBV_RATIO&quoteType=0&source=WEB&client=WEB'
#
# resp = requests.get(url, headers=headers)
# data = resp.text.replace('jQuery112305445752770008432_1694676002292(', '').replace(');', '')
# data_dict = json.loads(data)["result"]["data"]
# print(data_dict)

# 获取字段信息
# url = 'https://data.eastmoney.com/xg/xg/?mkt=kzz'
# resp = requests.get(url, headers=headers)
# soup = bs(resp.text, 'html.parser')
# data = soup.find("div", {"id": "dataview_kzz"}).find_all("th")
# data_sou = re.findall(r'[\u4e00-\u9fa5]', data)
# print(data_sou)