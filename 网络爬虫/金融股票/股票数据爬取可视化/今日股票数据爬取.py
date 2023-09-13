import requests
import csv
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar

# 保存csv
path = '今日股票趋势.csv'
file = open(path, mode="w", encoding='utf-8', newline="")
csv_f = csv.DictWriter(file,
                       fieldnames=['股票代码', '股票名称', '当前价', '涨跌额', '涨跌幅', '年初至今', '成交量', '成交额',
                                   '换手率',
                                   '市盈(TTM)', '股息率', '市值'])
# 写入表头
csv_f.writeheader()


def parse(res):
    for data in res['data']['list']:
        # 股票代码
        symbol = data['symbol']
        # 股票名称
        name = data['name']
        # 当前价
        current = data['current']
        # 涨跌额
        chg = data['chg']
        if chg:
            if float(chg) > 0:
                chg = "+" + str(chg)
            else:
                chg = str(chg)
        # 涨跌幅
        percent = str(data['percent']) + "%"
        # 年初至今
        current_year_percent = str(data['current_year_percent']) + "%"
        # 成交量
        volume = data["volume"]
        # 成交额
        amount = data['amount']
        # 换手率
        turnover_rate = str(data['turnover_rate']) + "%"
        # 市盈(TTM)
        pe_ttm = data['pe_ttm']
        # 股息率
        dividend_yield = data['dividend_yield']
        if dividend_yield:
            dividend_yield = str(dividend_yield) + "%"
        else:
            dividend_yield = None
        # 市值
        market_capital = data['market_capital']

        shares_dict = {'股票代码': symbol, '股票名称': name, '当前价': current,
                       '涨跌额': chg, '涨跌幅': percent, '年初至今': current_year_percent,
                       '成交量': volume, '成交额': amount, '换手率': turnover_rate,
                       '市盈(TTM)': pe_ttm, '股息率': dividend_yield,
                       '市值': market_capital}

        csv_f.writerow(shares_dict)


def spider():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.0.0 Safari/537.36"
    }
    for i in range(1, 10):
        print("=========正在爬取第" + str(i) + "页数据==========")
        # 拼接url，注意要使用 str
        url = "https://xueqiu.com/service/v5/stock/screener/quote/list?page=" + str(
            i) + "&size=30&order=desc&order_by=amount&exchange=CN&market=CN&type=sha&_=1601168743543"
        # 数据返回格式为json，所以要使用.json()，方便之后的数据获取
        response = requests.get(url=url, headers=headers).json()
        parse(response)


def echarts():
    # 读取csv文件
    data_df = pd.read_csv(path)
    df = data_df.dropna()
    df1 = df[['股票名称', '涨跌额']]
    # print(df1)
    # 取前30条数据
    df2 = df1.iloc[:30]
    # print(list(df2['成交量'].values))
    html = (
        Bar(init_opts=opts.InitOpts(width='100%', height="720px", page_title="股票数据可视化")).add_xaxis(
            list(df2['股票名称'].values))
        .add_yaxis('今日趋势', list(df2['涨跌额'].values))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="今日涨跌幅"),
            datazoom_opts=opts.DataZoomOpts()
        )
        .render("股票数据图.html")
    )
    return html


if __name__ == '__main__':
    spider()
    echarts()
