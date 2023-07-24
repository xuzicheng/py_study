import urllib.request

url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 1个类型和6个方法
print(type(response))  # <class 'http.client.HTTPResponse'>

# 11111按照一字节来读取，效率慢
# content = response.read()

# 22222返回5个字节
# content = response.read(5)
# print(content)

# 33333读一行
# content = response.readline()
# print(content)

# 44444读完
# content = response.readlines()
# print(content)

# 55555返回状态码,检测逻辑
print(response.getcode())    # 200 没错  404那些是错的

# 666666返回url地址
print(response.geturl())

# 77777返回状态信息
print(response.getheaders())



