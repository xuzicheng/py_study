# 使用urllib获取百度首页源码
import urllib.request

# 1_定义一个url 相当于目标地址
url = 'http://www.baidu.com'

# 2_模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3_获取响应中页面的源码
# read方法返回的是字节形式的二进制数据
# 要将二进制变成字符串=解码=decode（'编码的形式'）

content = response.read().decode('utf-8')
# 4_打印数据
print(content)
