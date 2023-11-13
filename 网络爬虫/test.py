import pandas as pd
import numpy as np


weather_df = pd.read_csv('E:\pythonProject\网络爬虫\JS逆向\gamer520\games.csv')

weather_df['三级下载地址'] = (weather_df['三级下载地址'].str.replace('\'', '').str.replace(': ', ':')
              .str.replace('点我  ', '').str.replace(' [立即下载]', '').str.replace('[', '').str.replace(']', '')
              .str.split('  '))

data_list = weather_df['三级下载地址'].values.tolist()
weather_df['三级下载地址'] = data_list[0][0]
weather_df['提取码'] = data_list[0][1]
weather_df['解压密码'] = data_list[0][-1]
weather_df.to_csv('test.csv')