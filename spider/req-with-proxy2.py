import requests
from lxml import etree
import pandas as pd

# 创建保存IP地址的列表
ip_list = []


def get_ip(url, headers):
    # 发送网络请求
    response = requests.get(url, headers=headers)
    response.encoding = 'UTF-8'
    # 判断请求是否成功
    if response.status_code == 200:
        # 解析HTML
        html = etree.HTML(response.text)
        # 获取所有带有IP的li标签
        li_all = html.xpath('//li[@class="f-list col-lg-12 col-md-12 col-sm-12 col-xs-12"]')
        # 遍历每行内容
        for li in li_all:
            # 获取IP
            ip = li.xpath('span@class="f-address"/text()')[0]
            # 获取端口
            port = li.xpath('span@class="f-port"/text()')[0]
            # 将IP与端口组合并添加到列表ip_list当中
            ip_list.append(ip + ':' + port)
            # 打印IP与端口
            print(f'代理IP:{ip},端口：{port}')



# 头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
}

if __name__ == '__main__':
    # 创建临时表格数据 ip_table
    ip_table = pd.DataFrame(columns=['ip'])
    for i in range(1, 5):
        # 获取免费代理IP的请求地址
        url = f'https://www.dieniao.com/FreeProxy/{i}.html'
        get_ip(url, headers)

    ip_table['ip'] = ip_list
    # 生成xlsx文件
    ip_table.to_excel('ip.xlsx', sheet_name='data')