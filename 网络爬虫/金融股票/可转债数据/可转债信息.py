import json
import re
import requests
from bs4 import BeautifulSoup as bs, Comment
from 请求配置信息 import dongFang
import warnings
warnings.filterwarnings('ignore')

resp_data, resp_field = dongFang()

# 获取字段信息
soup = bs(resp_field.text, 'html.parser')
print(soup.text)

# 可转债数据
data = resp_data.text.replace('jQuery112306648817856021285_1695195221752(', '').replace(');', '')
data_dict = json.loads(data)["result"]["data"]

