import json

import requests

# 1
# GET 带参请求
print('################')
print('GET 带参请求')
response = requests.get('http://httpbin.org/get?name=Jack&age=30')
print(response.content)





# requests模块中get和post请求的参数分别是params和data
# 2
# 配置Params参数
print('################')
print('配置Params参数')

data = {'name': 'Michael', 'age': '36'}
response = requests.get('http://httpbin.org/get', params=data)
print(response.content)






# 3
# POST 请求
print('################')
print('POST 请求')

# data参数的数据格式可以是列表、元组或者json
# 字典类型表单参数
data = {'1': '天生我材必有用', '2': '会当凌绝顶，一览众山小'}
# 将字典类型转换为json类型
data = json.dumps(data)
# 元组类型表单参数
#data = (('1', '天生我材必有用'), ("2", '会当凌绝顶，一览众山小'))
# 列表类型的表单参数
#data = [('1', '天生我材必有用'), ("2", '会当凌绝顶，一览众山小')]
response = requests.post('http://httpbin.org/post', data=data)
# 将响应数据转换为字典类型
response_dict = json.loads(response.text)
print(response_dict)





# 4
# 配置请求头
print('################')
print('配置请求头')
url = 'https://www.baidu.com'
# 创建头部信息
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
print(response.status_code)

