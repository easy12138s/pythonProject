import pandas as pd
from pandas import DataFrame
import json
from 网络爬虫.金融股票.请求配置信息 import dongFang
import warnings

warnings.filterwarnings('ignore')


def soup_kzz():
    resp_data = dongFang()

    # 获取字段信息
    field_df = pd.read_csv('可转债页面字段数据.csv', low_memory=False)

    # 可转债数据
    data = resp_data.text.replace('jQuery112306648817856021285_1695195221752(', '').replace(');', '')
    data_dict = json.loads(data)["result"]["data"]
    # 过滤掉不需要的列
    data_pd = DataFrame(data_dict).loc[:, field_df['英文名'].tolist()]
    data_pd.columns = field_df["中文名"]

    data_pd.to_csv("可转债信息.csv", encoding="utf-8")


def Last_Week_kzz(path, num):
    last_pd = pd.read_csv(path, low_memory=False)
    last_df = DataFrame(last_pd)
    return last_df.head(num).values


if __name__ == '__main__':
    soup_kzz()
    kzz_data = Last_Week_kzz("可转债信息.csv", 5)
    kzz_df = DataFrame(kzz_data)
    print(kzz_df)
