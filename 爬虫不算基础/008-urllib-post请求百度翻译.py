import urllib.request
import urllib.parse

# post请求  https://fanyi.baidu.com/sug

url = 'https://fanyi.baidu.com/sug'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}
# post请求的参数要进行编码 ，编码之后要调用encode方法 encode('utf-8')
data = urllib.parse.urlencode(data).encode('utf-8')
# 参数是放在请求定制的方法中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器
response = urllib.request.urlopen(request)
# print(response)

content = response.read().decode('utf-8')
print(content)
# print(type(content))  #str

# 字符串->json对象
import json

obj = json.loads(content)

print(obj)
