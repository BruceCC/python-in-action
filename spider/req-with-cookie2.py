import requests
from lxml import etree

cookies = 'JSESSIONID=D989301FD10C7EEEE050662AC18E43A8; csrfToken=b21c7ac3-4891-46fb-87a2-a4717849111d'

headers = {
    'Host': '10.11.32.156:7777',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 创建requestsCookieJar对象，用于设置Cookies信息
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.strip().split('=', 1)
    cookies_jar.set(key, value)

# 发送网络请求
url = 'http://10.11.32.156:7777/wiki/view/ai-teck/topic/79884'
response = requests.get(url, headers=headers, cookies=cookies_jar)
response.encoding = 'utf-8'
#print(response.text)
if response.status_code == 200:
    # 解析html代码
    html = etree.HTML(response.text)
    # 获取用户名
    name = html.xpath('//div[@class="profile-sidebar-item profile-info"]//span[@class="h5 bold"]//text()')
    print(name[0])



for i in range(50):
    try:
        response = requests.get(url, headers=headers, cookies=cookies_jar, timeout=0.05)
        response.encoding = 'UTF-8'
        print(response.status_code)
        print(response.text)
        if response.status_code == 200:
            # 解析html代码
            html = etree.HTML(response.text)
            # 获取用户名
            name = html.xpath('//div[@class="profile-sidebar-item profile-info"]//span[@class="h5 bold"]//text()')
            print(name[0])
    except Exception as e:
        # 打印异常信息
        print('异常' + str(e))




