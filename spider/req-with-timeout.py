import requests

# 向百度循环发送50次http
for i in range(50):
    try:
        response = requests.get('http://www.baidu.com', timeout=0.05)
        response.encoding = 'utf-8'
        print(response.status_code)
    except Exception as e:
        # 打印异常信息
        print('异常' + str(e))

