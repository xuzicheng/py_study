# 应用场景：多个参数

# https://cn.bing.com/search?q=蔡徐坤&sex=男
import urllib.parse
#
# data = {
#     'q': '蔡徐坤',
#     'sex': '男'
# }
# a = urllib.parse.urlencode(data)
# print(a)


import urllib.request

base_url = 'https://cn.bing.com/search?'

data = {
    'q': '蔡徐坤',
    'sex': '男'
}

new_data = urllib.parse.urlencode(data)
print(new_data)

# 请求资源路径
url = base_url + new_data

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 定制
request = urllib.request.Request(url=url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request)
# 获取数据
content = response.read().decode('utf-8')
print(content)
