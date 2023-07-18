import requests_cache
import time

# 获取equests_cache模块当前的版本
print(f'requests-cache模块版本为：{requests_cache.__version__}')

# 设置缓存
requests_cache.install_cache()

# 清理缓存
requests_cache.clear()


# 定义钩子函数
def make_throttle_hook(timeout=0.1):
    def hook(response, *args, **kwargs):
        # 打印请求结果
        print(f'请求结果：{response.text}')
        # 判断没有缓存就添加延时
        if not getattr(response, 'from_cache', False):
            print('等待', timeout, '秒！')
            time.sleep(timeout)
        else:
            print('是否存在使用缓存！', response.from_cache)
        return response

    return hook


if __name__ == '__main__':
    # 创建缓存
    requests_cache.install_cache()
    # 清理缓存
    requests_cache.clear()
    # 创建缓存会话
    s = requests_cache.CachedSession()
    # 配置钩子函数
    s.hooks = {'response': make_throttle_hook(2)}
    # 模拟第一次发送网络请求
    r = s.get('https://httpbin.org/get')
    print(r.from_cache)
    # 模拟第二次发送网络请求
    r = s.get('https://httpbin.org/get')
    print(r.from_cache)
    # 模拟第三次发送网络请求
    r = s.get('https://httpbin.org/get')
    print(r.from_cache)
    # 模拟第四次发送网络请求
    r = s.get('https://httpbin.org/get')
