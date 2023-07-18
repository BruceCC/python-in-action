import requests

# 设置header头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# proxy
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080'
}

# 对需要爬取的网络发送请求，verify-False不验证服务器的SSL证书，要有try catch异常捕获
try:
    response = requests.get('http://2023.ip138.com', headers=headers, proxies=proxies, verify=False, timeout=3)
    response.encoding = 'UTF-8'
    print(response.text)
except Exception as e:
    print('错误异常信息为：', e)


