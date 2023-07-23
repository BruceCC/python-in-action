from lxml import etree
import time
import random
import requests

# 头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}


# 处理字符串中的空白字符，并拼接字符串
def processing(strs: str):
    # 定义保存内容的字符串
    s = ''
    for n in strs:
        # 去除空字符串
        n = ''.join(n.split())
        # 拼接字符串
        s = s + n
    # 返回拼接后的字符串
    return s


# 获取电影信息
def get_movie_info(url: str):
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    div_all = html.xpath('//div[@class="info"]')
    for div in div_all:
        # 获取电影名字相关信息
        names = div.xpath('./div[@class="hd"]/a//span/text()')
        # 处理电影名称信息
        name = processing(names)
        # 获取导演、演员信息
        infos = div.xpath('./div[@class="bd"]/p/text()')
        info = processing(infos)
        # 获取电影评分
        score = div.xpath('./div[@class="bd"]/div/span[2]/text()')
        # 获取评价人数
        eleluation = div.xpath('./div[@class="bd"]/div/span[4]/text()')
        # 获取电影总结文字
        summary = div.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')

        print(f"电影名称：{name}")
        print(f"导演与演员：{info}")
        print(f"电影评分：{score}")
        print(f"电影总结：{summary}")
        print(f"评价人数：{eleluation}")
        print(f"-----------------分割线------------------------")


if __name__ == "__main__":
    # 每25页为间隔，实现循环，共10页
    # 通过format替换切换页码url地址
    for i in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={i}&filter='
        # 调用爬虫方法获取电影信息
        get_movie_info(url)
        # 等待1-3秒随机时间
        time.sleep(random.randint(1, 3))
