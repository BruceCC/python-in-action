import re

# search 结果是match对象
print(r'### search')
pattern = 'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)
print(match)

string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern, string,)
print(match)

# \b边界匹配
print(r'### \b边界匹配')
pattern = r'\bmr\b'
print(re.search(pattern, 'mrsoft'))
print(re.search(pattern, 'mr soft'))


# findall 结果是列表
print(r'### findall')
pattern = 'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall(pattern, string, re.I)
print(match)


# 贪婪匹配
# .*贪婪匹配
print(r'### .*贪婪匹配')
pattern = 'https://.*/'
match = re.findall(pattern, 'https://baidu.com/')
# 打印匹配的所有内容
print(match)
# 只打印匹配的中间内容
pattern = 'https://(.*)/'
match = re.findall(pattern, 'https://baidu.com/')
print(match)

# 非贪婪匹配
print(r'### 非贪婪匹配')
pattern = 'https://.*(\d+).com/'
match = re.findall(pattern, 'https://baidu123.com/')
print(match)
pattern = 'https://.*?(\d+).com/'
match = re.findall(pattern, 'https://baidu123.com/')
print(match)


# 替换字符串
print('### 替换字符串')
# 手机号脱敏
china_mobile_pattern = r'(\b(?:13\d|14[014-9]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9]))\d{4}(\d{4}\b)'
text = '我的手机号码是：13812345678，还有一个备用号码：13987654321'
result = re.sub(china_mobile_pattern, r'\1****\2', text)
print(result)
result = re.subn(china_mobile_pattern, r'\1****\2', text, flags=re.I)
print(result)
print(result[1])


# 分割字符串
print('### 分割字符串')
url = 'https://movie.douban.com/annual/2022?fullscreen=1&source=navigation'
pattern = r'[?|&]'
print(re.split(pattern, url))
print(re.split(pattern, url, maxsplit=1))




