import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)


# 一个类型和六个属性
print(type(response))

# 设置响应编码格式
response.encoding='utf-8'

# 以字符串形式返回网页源码
print(response.text)


# 返回url路径
print(response.url)


#  返回二进制数据
print(response.content)

# 返回响应状态码
print(response.status_code)


# 返回响应头
print(response.headers)