import json
import requests
import base64

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Referer': 'http://report.itophis.com/web/attendance/dist/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}

params = {
    't': '1698043869847',
}

response = requests.get('http://report.itophis.com/attendance/sys/auth/captcha', params=params, headers=headers, verify=False)
data = json.loads(response.text)

png_data = data['data']['image'][22:]

base_png = base64.b64decode(png_data)
with open('./images/topcheer.png', 'wb') as f:
    f.write(base_png)



