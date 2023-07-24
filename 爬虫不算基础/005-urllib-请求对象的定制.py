import urllib.request

url = 'https://www.baidu.com'

# url的组成    https://www.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6
# http/https     www.baidu.com        80/443         search    q=%E5%91%A8%E6%9D%B0%E4%BC%A6
#      协议            主机             端口号            路径                  参数                   锚点


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 请求对象的定制 ，因为urlopen方法中不能存储字典,所以headers无法存入
# 因为参数顺序问题，不能直接写，要用关键字传递参数
request = urllib.request.Request(url=url, headers=headers)
#######################################

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
