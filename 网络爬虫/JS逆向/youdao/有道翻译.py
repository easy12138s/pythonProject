# encoding: utf-8
"""
    @version: python3.1
    @author:'EASY'
    @contact: 2382019442@qq.com
    @software: PyCharm
    @file: 有道翻译.py
    @time: 2023/10/17 10:20
"""
import base64
import hashlib
import json
import subprocess
import time
from functools import partial

import requests
#  pip3 install -i https://mirrors.aliyun.com/pypi/simple/ pycryptodome  使用阿里镜像
from Crypto.Cipher import AES

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')


def youDao_resp(i):
    # 请求加密主要为keyfrom、sign
    # keyfrom为当前时间戳，sign为MD5加密后的密文
    localtime = str(int(time.time() * 1000))
    data = "client=fanyideskweb&mysticTime={}&product=webfanyi&key=fsdsogkndfokasodnaso".format(localtime)
    sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()

    cookies = {
        'P_INFO': 'null',
        'OUTFOX_SEARCH_USER_ID': '-997082143@10.110.96.153',
        'OUTFOX_SEARCH_USER_ID_NCOO': '1926107383.121204',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'P_INFO=null; OUTFOX_SEARCH_USER_ID=-997082143@10.110.96.153; OUTFOX_SEARCH_USER_ID_NCOO=1926107383.121204',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'i': i,
        'from': 'auto',
        'to': '',
        'dictResult': 'true',
        'keyid': 'webfanyi',
        'sign': sign,
        'client': 'fanyideskweb',
        'product': 'webfanyi',
        'appVersion': '1.0.0',
        'vendor': 'web',
        'pointParam': 'client,mysticTime,product',
        'mysticTime': localtime,
        'keyfrom': 'fanyi.web',
        'mid': '1',
        'screen': '1',
        'model': '1',
        'network': 'wifi',
        'abtest': '0',
        'yduuid': 'abcdefg',
    }

    response = requests.post('https://dict.youdao.com/webtranslate', cookies=cookies, headers=headers, data=data)
    return response.text


def youDao_decry(i):
    # 请求获取的密文解密
    ciphertext_date = youDao_resp(i)

    # js解密
    # path = os.path.dirname(os.path.abspath(__file__))
    # js_path = os.path.join(path, 'js\有道翻译.js')
    #
    # with open(js_path, 'r', encoding='utf-8') as f:
    #     signs = execjs.compile(f.read()).call('getDatas', ciphertext_date)
    #     text = json.loads(signs)
    #
    # return text['translateResult'][0][0]['tgt']

    # python解密
    o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
    n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

    a = hashlib.md5(o.encode()).digest()
    r = hashlib.md5(n.encode()).digest()
    t = ciphertext_date.replace("_", "/").replace("-", "+")
    # 数据必须在 CBC 模式下填充到 16 字节边界
    missing_padding = 4 - len(t) % 4
    if missing_padding:
        t += '=' * missing_padding

    cipher = AES.new(a, AES.MODE_CBC, r)
    decrypted = cipher.decrypt(base64.b64decode(t)).decode('utf-8')
    index = decrypted.rfind("}")
    decrypted = decrypted[:index + 1]
    text = json.loads(decrypted)
    return text['translateResult'][0][0]['tgt']


if __name__ == '__main__':
    fanyi = youDao_decry('hello,world!')
    print(fanyi)
