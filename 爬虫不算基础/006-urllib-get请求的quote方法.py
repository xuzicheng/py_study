# 获取https://cn.bing.com/search?q=蔡徐坤网页的源码


import urllib.request
import urllib.parse

url = 'https://cn.bing.com/search?q='

# 将蔡徐坤变成unicode编码格式
# 需要依赖于urllib.parse
name = urllib.parse.quote('蔡徐坤')
url = url+name

# 请求对象定制
headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应内容
content = response.read().decode('utf-8')

# 打印
print(content)




