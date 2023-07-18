from requests_html import HTMLSession

# 创建HTML会话对象
session = HTMLSession()

# 访问目标网页
r = session.get('http://10.11.32.156:7777/wiki/view/ai-teck/topic/79884')

print(r.html)

print(r.text)


