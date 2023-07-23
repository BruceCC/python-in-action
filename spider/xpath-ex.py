from lxml import etree
import requests

# 地址
url = 'https://movie.douban.com/top250'
# 头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

response = requests.get(url, headers=headers)
response.encoding = 'UTF-8'

if response.status_code == 200:
    html = etree.HTML(response.text)
    print('##########################直接打印requests结果################################')
    print(response.text)
    html_text = etree.tostring(html, encoding='utf-8')
    # 打印整个网页
    print('##########################打印整个网页################################')
    print(html_text.decode('utf-8'))

    # 获取所有节点
    print('##########################获取所有节点################################')
    print(r'使用//* 获取所有节点')
    node_all = html.xpath('//*')
    # 打印数据类型
    print(f'数据类型：{type(node_all)}')
    # 打印数据长度
    print(f'数据长度：{len(node_all)}')
    # 打印数据内容
    print(f'数据内容：{node_all}')
    # 通过推导式打印所有节点名称，通过节点对象.tag获取节点名称
    print(f'节点名称：{[i.tag for i in node_all]}')
    print('##########################获取指定类型的节点################################')
    print(r'获取所有a标签')
    # 获取所有a标签
    li_all = html.xpath('//a')
    # 打印所有li节点
    print(f'所有li节点：{li_all}')
    # 打印指定li节点
    print(f'指定li节点：{li_all[1]}')
    li_txt = etree.tostring(li_all[1], encoding='utf-8')
    print(f'获取指定节点html代码{li_txt.decode("utf-8")}')

    print('##########################获取直接子节点################################')
    print(r'使用/获取直接子节点')
    print(html.xpath('//li/div'))

    print('##########################获取子孙节点################################')
    print(r'使用//获取子孙节点')
    print(html.xpath('//li//a'))

    print('##########################获取父节点################################')
    print(r'使用..获取父节点')
    print(f'所有a的父节点：{html.xpath("//a//..")}')

    print('##########################获取文本################################')
    print(r'使用text()获取文本')
    print(f'获取文本点：{html.xpath("//a//text()")}')

    print('##########################属性匹配################################')
    print(r'使用[@...]实现节点属性匹配')
    a = html.xpath('//a[@href="https://movie.douban.com/subject/1292052/"]')
    print(a)
    print(html.xpath('//a/@href'))
    title = html.xpath('//a[@href="https://movie.douban.com/subject/1292052/"]/span[@class="title"]/text()')
    print(title)

    print('##########################属性多值匹配、模糊匹配################################')
    # 创建lxml的etree对象，将HTML作为输入
    html = '''
    <html>
      <body>
        <a href="https://example.com">Example 1</a>
        <a href="https://google.com">Example 2</a>
        <a href="https://baidu.com">Example 3</a>
      </body>
    </html>
    '''
    tree = etree.HTML(html)

    # 使用XPath匹配<a>标签中href值为"https://baidu.com"
    matching_a_tags = tree.xpath('//a[@href="https://baidu.com"]')

    # 输出结果
    for a_tag in matching_a_tags:
        print(etree.tostring(a_tag, encoding='utf-8').decode('utf-8'))

    # 创建 lxml 的 etree 对象，将 HTML 作为输入
    html = '''
    <html>
      <body>
        <div class="level1">Level 1</div>
        <div class="level2 red" alt="test">Level 2</div>
        <div class="level3 yellow">Level 3</div>
        <div class="level4" id="ll4">Level 4</div>
        <div class="level5" title="ll5 title">Level 5</div>
      </body>
    </html>
    '''
    tree = etree.HTML(html)

    # 使用 XPath 获取所有 class 属性值中包含 "level" 的 div 节点的文本信息
    div_nodes = tree.xpath('//div[contains(@class, "level")]')
    # 同时满足多个条件
    div_ll4 = tree.xpath('//div[contains(@class, "level") and @id="ll4"]')
    # 获取第五个div的title值
    div5_title = tree.xpath('//body/div[5]/@title')
    print(f'获取第五个div的title值: {div5_title}')
    div1_text = tree.xpath('//body/div[last()]')
    print(f'获取最后一个div的内容: {div1_text[0].text}')
    div4_text = tree.xpath('//body/div[last()-1]')
    print(f'获取倒数第二个div的内容: {div4_text[0].text}')
    div2_text = tree.xpath('//div[position() = 2]/@alt')
    print(f'获取第二个div的内容: {div2_text}')

    print(f'div_ll4: {div_ll4[0].text}')

    # 输出结果
    for div_node in div_nodes:
        text = div_node.text
        print(text)








