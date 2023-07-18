import requests_cache
import requests

# 获取equests_cache模块当前的版本
print(f'requests-cache模块版本为：{requests_cache.__version__}')

# 设置缓存
requests_cache.install_cache()

# 清理缓存
requests_cache.clear()

# 定义测试地址url
url = 'http://httpbin.org/get'

# 第一次发送网络请求
response = requests.get(url)

# 判断是否存在缓存
print(f'第一次发送网络请求，是否存在缓存：{response.from_cache}')

# 第二次发送网络请求
response = requests.get(url)

# 判断是否存在缓存
print(f'第二次发送网络请求，是否存在缓存：{response.from_cache}')



