from requests_html import HTMLSession, UserAgent

# 创建HTML会话对象
session = HTMLSession()

# 生成随机头部信息
ua = UserAgent().random

print(ua)


r = session.get('https://movie.douban.com/chart', headers={'user-agent': ua})
r.encoding = 'UTF-8'


if r.status_code == 200:
    # 调用render
    r.html.render()
    # 获取当前页面中所有电影信息的a标签
    class_wp = r.html.xpath('//div[@class="list-wp"]/a')
    for a in class_wp:
        # 获取电影名称
        title = a.find('p span')[0].text
        # 获取电影评分
        score = a.find('span')[1].text
        # 获取详情页URL
        detail_url = a.attrs.get("href")
        # 获取图片URL
        img_url = a.find('img')[0].attrs.get("src")
        print(f'名称：{title}')
        print(f'评分：{score}')
        print(f'详情：{detail_url}')
        print(f'图片：{img_url}')
else:
    print('请求失败')












































































































