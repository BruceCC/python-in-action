from requests_html import HTMLSession, UserAgent

# 创建HTML会话对象
session = HTMLSession()

# 生成随机头部信息
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

print(ua)


r = session.get('http://10.11.33.235:10001/#/home/download', headers={'user-agent': ua})
r.encoding = 'UTF-8'

print(r.text)







