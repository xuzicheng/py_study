# 1：获取网页源码
# 2：解析    解析服务器响应文件 etree.html
# 3：打印

import urllib.request

url = 'https://www.baidu.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(headers=headers, url=url)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# 解析源码 获取需要数据
from lxml import etree

tree = etree.HTML(content)

# 获取数据 xpath的返回值是一个列表类型的数据,可以访问下标去掉括号
result = tree.xpath('//input[@id="su"]/@value')[0]

print(result)
