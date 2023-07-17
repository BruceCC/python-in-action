import requests

# 发送网络请求
print('################')
print('返回内容UTF-8编码')
response = requests.get('https://www.baidu.com')
response.encoding = 'utf-8'

print(f'响应状态码：{response.status_code}')
print(f'请求网络地址：{response.url}')
print(f'响应状态码：{response.headers}')
print(f'响应状态码：{response.cookies}')
print(f'相应内容：{response.text}')


# 爬取二进制数据
print('################')
print('爬取二进制数据')
response = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
print(response.content)
with open('百度logo.png', 'wb') as f:
    f.write(response.content)









