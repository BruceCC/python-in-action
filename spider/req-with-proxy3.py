import requests
import pandas
from lxml import etree

# 读取代理ip文件内容
ip_table = pandas.read_excel('ip.xlsx')
# 获取代理ip列信息
ip_list = ip_table['ip']

# 头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

# 循环遍历代理信息并通过代理发送网络请求
for ip in ip_list:
    proxies = {
        'http': f'http://{ip}',
        'https': f'https://{ip}'
    }

    try:
        response = requests.get('http://2023.ip138.com/', headers=headers, proxies=proxies, timeout=2)
        print(response.status_code)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            html = etree.HTML(response.text)
            info = html.xpath('/html/body/p[1]//text()')
            # 输出当前IP匿名信息
            print(info)
    except Exception as e:
        print(ip + '不可用')
