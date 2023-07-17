import requests
# 导入requests.exceptions模块中的三种异常类
from requests.exceptions import RequestException, ConnectionError, Timeout, HTTPError, ReadTimeout


# 循环发送请求50次，要有异常捕获
for i in range(50):
    try:
        response = requests.get('https://www.baidu.com', timeout=0.05)
        print(response.status_code)
    except ReadTimeout:
        print('超时异常')
    except HTTPError:
        print('httperror')
    except RequestException:
        print('reqerror')

