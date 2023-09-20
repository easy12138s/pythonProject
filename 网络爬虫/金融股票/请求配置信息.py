"""
    爬虫请求头配置信息
"""
import requests


# 东方财富可转债
def dongFang():
    cookies = {
        'qgqp_b_id': 'e943d73977c5642211ae816d6df7f2ef',
        'st_si': '20123219818259',
        'st_asi': 'delete',
        'JSESSIONID': '6EEA5A47B18477D75D3E7D5A7BEAB3C9',
        'st_pvi': '56500704703528',
        'st_sp': '2022-12-06%2015%3A57%3A11',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '6',
        'st_psi': '20230920153058675-113300300986-2060725315',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'qgqp_b_id=e943d73977c5642211ae816d6df7f2ef; st_si=20123219818259; st_asi=delete; JSESSIONID=6EEA5A47B18477D75D3E7D5A7BEAB3C9; st_pvi=56500704703528; st_sp=2022-12-06%2015%3A57%3A11; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=6; st_psi=20230920153058675-113300300986-2060725315',
        'Referer': 'https://data.eastmoney.com/xg/xg/?mkt=kzz',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'callback': 'jQuery112306648817856021285_1695195221752',
        'sortColumns': 'PUBLIC_START_DATE',
        'sortTypes': '-1',
        'pageSize': '50',
        'pageNumber': '1',
        'reportName': 'RPT_BOND_CB_LIST',
        'columns': 'ALL',
        'quoteColumns': 'f2~01~CONVERT_STOCK_CODE~CONVERT_STOCK_PRICE,f235~10~SECURITY_CODE~TRANSFER_PRICE,f236~10~SECURITY_CODE~TRANSFER_VALUE,f2~10~SECURITY_CODE~CURRENT_BOND_PRICE,f237~10~SECURITY_CODE~TRANSFER_PREMIUM_RATIO,f239~10~SECURITY_CODE~RESALE_TRIG_PRICE,f240~10~SECURITY_CODE~REDEEM_TRIG_PRICE,f23~01~CONVERT_STOCK_CODE~PBV_RATIO',
        'quoteType': '0',
        'source': 'WEB',
        'client': 'WEB',
    }
    url_field = 'https://data.eastmoney.com/xg/xg/?mkt=kzz'
    url_data = 'https://datacenter-web.eastmoney.com/api/data/v1/get'
    response_data = requests.get(url_data, params=params, cookies=cookies, headers=headers)
    response_field = requests.get(url_field, params=params, cookies=cookies, headers=headers)

    return response_data
    # response_field
