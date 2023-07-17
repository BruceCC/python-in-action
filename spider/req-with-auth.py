import requests
from requests.auth import HTTPBasicAuth

# 定义请求地址
url = "http://sck.rjkflm.com:666/spider/auth/"

# 创建httpbasic对象，请求参数为用户名密码
ah = HTTPBasicAuth('admin', 'admin')

response = requests.get(url, auth=ah)
response.encoding = 'utf-8'

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)
