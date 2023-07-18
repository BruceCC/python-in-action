import requests
from lxml import etree

cookies = 'wps_sid=ef4bf90ea0750cd68261072e7150440c10b5ed2600000000f4; csrf=dmmEzYB5Rta4dcMSpkZwT4B4eRe8biEN; wps_domain=chinaums.com; yuyanname=jian; GEONGF_SESSIONID=egNjHI7RVH1PUpgB5wbYvYokHGd_drRk3OzC422jxlpE6KRc1Z49!1553153182; fp_ver=4.7.1; BSFIT_EXPIRATION=1689620799693; BSFIT_OkLJUJ=FHGi1xWBV092W1ZmePidaZqJQB0iGPXj; BSFIT_DEVICEID=lXzrgoO3FiAuIUQ0fqkbsyC2M3u-7bSaO9vxZxmqKuPEyouwcw-WnCq88eNzP7M2mBxRSrmv9tR4g5ioCyNAGkLAAbIIPgngDU4GCcPBOxhf50r-TlOV1aFna8F5bUCHnmx-uuxg_MCyV98WGfSLyAR7OYFvgSa3; userSession=28a3db7af3f78c1febb2b438ba1932795556e427409213cc1e1be58c6c493d9b43db0ebd5ba06a23c85b5a2d61f8054f1f7f664f9d34b2252159c1eade456213f5c891ac5fc025ccdf2dd3907a0a8a1ad4cc1501a414e37eda34422cb35f7ba3d881e6b388022b37a2c221a1707a75b6eb5ca46aa99398bedd58d2a1920611864e61a85297d203fa80e2c0e7e3d739fd6c919933e476eeed; userSession2=neo###2023-07-17 17:09:55###000120438043###000120438043'
headers = {
    'Host': 'www.chinaums.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# 创建requestsCookieJar对象，用于设置Cookies信息
cookies_jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key, value = cookie.strip().split('=', 1)
    cookies_jar.set(key, value)

# 发送网络请求
url = 'https://www.chinaums.com/'
response = requests.get(url, headers=headers, cookies=cookies_jar)
response.encoding = 'UTF-8'
#print(response.text)
if response.status_code == 200:
    # 解析html代码
    html = etree.HTML(response.text)
    # 获取用户名
    name = html.xpath('//div[@class="top_left hidden-xs"]/a[1]')
    print(name[0])




