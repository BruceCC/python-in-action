import requests

# 创建会话对象
session = requests.Session()

# 登录
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
data = {'username': 'mrsoft', 'password': 'mrsoft'}
# 发送登录请求
response = session.post(url, data=data)
response.encoding = 'utf-8'
# 发送登录后页面请求
response2 = session.get('http://site2.rjkflm.com:666')
response2.encoding = 'utf-8'

print('登录信息：', response.text)
print('登录后页面信息：', response2.text)

