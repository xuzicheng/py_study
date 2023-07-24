import urllib.request

# 下载一个网页
url_page = 'http://www.baidu.com'
urllib.request.urlretrieve(url_page, 'baidu.html')

# 图片
url_image = 'https://th.bing.com/th/id/OIP.YUxhOCth9WDXOj3FYfwHpwHaHa?w=169&h=180&c=7&r=0&o=5&dpr=2&pid=1.7'
urllib.request.urlretrieve(url_image, filename='cxk.jpg')

# 视频  b站下载不了，反爬虫
url_video = 'blob:https://www.bilibili.com/9851aa1d-8455-4624-97c0-e8ddc2170cd3'
urllib.request.urlretrieve(url_video, 'bili.mp4')




