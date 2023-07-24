# get请求
import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)

# 获取响应数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# 数据下载到本地  open方法默认使用gbk编码，要想保存汉子，需要指定utf-8编码
# fp=open('douban.json','w',encoding='utf-8')
# fp.write(content)

with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
