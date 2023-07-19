from requests_html import HTMLSession, UserAgent

# 创建HTML会话对象
session = HTMLSession()

# 生成随机头部信息
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

print(ua)


r = session.get('https://www.chinaums.com/xwzx/gsxw/', headers={'user-agent': ua})
r.encoding = 'UTF-8'

print(r.text)

# 判断请求是否成功，成功则打印响应内容
if r.status_code == 200:
    # 获取所有class=right_li中的<li>标签
    li_all = r.html.xpath('//li[@class="right_li"]')

    # 循环遍历每个LI标签
    for li in li_all:
        # 提取新闻标题内容
        news_title = li.find('a')[0].find('span')[0].text
        # 获取新闻详情对应的地址
        news_href = 'https://www.chinaums.com/xwzx/gsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('.')
        # 获取新闻发布时间
        news_time = li.find('a')[0].find('em')[0].text
        print(f'新闻标题：{news_title}\n')
        print(f'新闻时间：{news_time}\n')
        print(f'新闻链接：{news_href}\n')


    # 获取特定内容新闻
    for li in r.html.find('li', containing='项目'):
        # 提取新闻标题内容
        news_title = li.find('a')[0].find('span')[0].text
        # 获取新闻详情对应的地址
        news_href = 'https://www.chinaums.com/xwzx/gsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('.')
        # 获取新闻发布时间
        news_time = li.find('a')[0].find('em')[0].text
        print(f'新闻标题：{news_title}\n')
        print(f'新闻时间：{news_time}\n')
        print(f'新闻链接：{news_href}\n')

        # 使用search方法获取
        for li in r.html.find('li', containing='项目'):
            # 提取新闻标题内容
            news_title = li.search('<span class="right_span">{}</span>')[0]
            # 获取新闻详情对应的地址
            news_href = 'https://www.chinaums.com/xwzx/gsxw/' + li.search('<a href="{}" target="_blank" class="right_a">')[0].lstrip('./')
            # 获取新闻发布时间
            news_time = li.search('<em class="right_em">{}</em>')[0]
            print(f'新闻标题：{news_title}\n')
            print(f'新闻时间：{news_time}\n')
            print(f'新闻链接：{news_href}\n')















