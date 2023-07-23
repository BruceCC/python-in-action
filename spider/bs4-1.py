from bs4 import BeautifulSoup

# HTML 示例字符串
html = '''
<html>
  <head>
    <title>示例页面</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">

    <link rel="apple-touch-icon" href="https://img1.doubanio.com/f/movie/d59b2715fdea4968a450ee5f6c95c7d7a2030065/pics/movie/apple-touch-icon.png">
    <link href="https://img1.doubanio.com/f/movie/49be52183082540604939d7fbbf80b17ca8abd0b/dist/movie/charts/top_movies.css" rel="stylesheet" type="text/css">
  </head>
  <body>
    <h1>欢迎使用 BeautifulSoup</h1>
    <div class="content">
      <p>这是一个示例页面。</p>
      <ul>
        <li>列表项1</li>
        <li>列表项2</li>
        <li>列表项3</li>
      </ul>
    </div>
  </body>
</html>
'''

# 创建 BeautifulSoup 对象
# soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, features='lxml')

# 使用 BeautifulSoup 提取信息
title = soup.title.text
heading = soup.h1.text
paragraph = soup.div.p.text
list_items = [li.text for li in soup.ul.find_all('li')]

# 打印提取的信息
print("标题:", title)
print("soup.title.string:", soup.title.string)
print("soup.title.name:", soup.title.name)
print("标题:", heading)
print("段落:", paragraph)
print("列表项:")
for item in list_items:
    print("-", item)


print(f'meta节点中属性如下：{soup.meta.attrs}')
print(f'link节点中属性如下：{soup.link.attrs}')
print(f'div节点中属性如下：{soup.div.attrs}')
print(f'meta中http-equiv对应的值：{soup.meta["http-equiv"]}')
print(f'link中href对应的值：{soup.link["href"]}')



