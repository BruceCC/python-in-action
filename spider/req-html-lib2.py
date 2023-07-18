from requests_html import HTMLSession, UserAgent

# 创建HTML会话对象
session = HTMLSession()

# 模拟表单登录的数据
data = {
    'username': 'admin',
    'password': '123456'
}

# 生成随机头部信息
#ua = UserAgent.random

# 发送post请求
r = session.post('http://httpbin.org/post', data=data)
#r = session.post('http://10.11.32.156:7777/wiki/view/ai-teck/topic/79884', data=data, headers={'user-agent': ua})

# 判断请求是否成功，成功则打印响应内容
if r.status_code == 200:
    print(r.text)
else:
    print('请求失败')





