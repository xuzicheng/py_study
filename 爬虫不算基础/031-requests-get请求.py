import requests

url = 'https://www.baidu.com/s'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

data = {
    'wd': '北京'
}

# url    资源路径
# params 参数    参数无需urlencode编码
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)

content = response.text
print(content)


