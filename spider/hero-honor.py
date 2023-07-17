import requests
from lxml import etree
import os
import time
import random

# 统计程序运行时间
start_time = time.time()

print('===>开始下载王者荣耀皮肤...')

# 发送的地址
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}


# 发送请求
# 获取英雄列表信息
hero_list_resp = requests.get(hero_list_url, headers=headers)
print(hero_list_resp.json())

# 处理结果
hero_num = 0
hero_pic_dir_name = "hero_skin"
if not os.path.exists(hero_pic_dir_name):
    os.mkdir(hero_pic_dir_name)
for h in hero_list_resp.json():
    hero_num += 1
    ename = h.get("ename")
    cname = h.get("cname")
    print(f"开始下载{ename}-{cname}\n")

    # 每个英雄的皮肤单独建立一个文件保存，同时根目录保存一份方便浏览全部
    single_hero_path = hero_pic_dir_name + "/" + cname
    if not os.path.exists(single_hero_path):
        os.mkdir(single_hero_path)

    # 访问英雄主页
    hero_info_url = f"https://pvp.qq.com/web201605/herodetail/{ename}.shtml"
    hero_info_resp = requests.get(hero_info_url, headers=headers)
    hero_info_resp.encoding = "gbk"
    e = etree.HTML(hero_info_resp.text)
    skin_names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]

    try:
        skin_names = [name[0:name.index('&')] for name in skin_names.split('|')]
    except:
        print(f"{cname}皮肤名称解析异常\n")
        continue

    for i, name in enumerate(skin_names):
        print(f"下载{cname}-{name}\n")
        hero_pic_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i}.jpg'
        hero_pic_resp = requests.get(hero_pic_url, headers=headers)

        # 接收服务器响应的图片并保存
        with open(f"{hero_pic_dir_name}/{cname}-{name}.jpg", 'wb') as f:
            f.write(hero_pic_resp.content)
        with open(f"{single_hero_path}/{name}.jpg", 'wb') as f:
            f.write(hero_pic_resp.content)

        time.sleep(random.randint(1, 5))

    print(f"完成下载{ename}-{cname}\n")

print(f"total heros: {hero_num}")
# 解析相应的数据

# 是否保存

end_time = time.time()
# 程序的运行时间，单位为秒
run_time = end_time - start_time
print(f'完成所有皮肤下载，总耗时：{run_time}')



