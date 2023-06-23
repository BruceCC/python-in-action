from flask import Flask, render_template, request
import requests as http_request
from lxml import etree

mobile_query_app = Flask(__name__)

data = {"mobile": "", "location": "", "operator": "", "card_type": "", "area": "", "code": ""}

@mobile_query_app.route('/')
def index():
    # return "hello!"
    return render_template('index.html', data=data)

@mobile_query_app.route('/query')
def query():
    mobile = request.args.get('mobile')
    getMobile(mobile)

    return render_template('index.html', data=data)


def getMobile(mobile):
    if len(mobile) == 0:
        return
    url = f'https://ip138.com/mobile.asp?mobile={mobile}&action=mobile'
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

    resp = http_request.get(url, headers=headers)
    resp.encoding = 'utf-8'
    print(resp.text)

    e = etree.HTML(resp.text)
    data["mobile"] = e.xpath('//div[@class="table"]/table/tbody/tr[1]/td[2]/a[1]/text()')[0]
    data["location"] = e.xpath('//div[@class="table"]/table/tbody/tr[2]/td[2]/span/text()')[0]
    data["operator"] = e.xpath('//div[@class="table"]/table/tbody/tr[3]/td[2]/a/text()')[0]
    #data["card_type"] = e.xpath('//div[@class="table"]/table/tbody/tr[4]/td[2]/a/text()')[0]
    data["area"] = e.xpath('//div[@class="table"]/table/tbody/tr[5]/td[2]/a/text()')[0]
    data["code"] = e.xpath('//div[@class="table"]/table/tbody/tr[6]/td[2]/a/text()')[0]
    print(f'!!!!!!!!!!!!!!!!!!!!\n{data}')

#mobile_query_app.run(debug=True)
mobile_query_app.run(debug=False)
