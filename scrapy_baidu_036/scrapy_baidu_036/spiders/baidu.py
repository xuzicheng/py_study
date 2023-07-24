import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫的时候使用的值
    name = "baidu"
    # 允许访问的域名
    allowed_domains = ["www.baidu.com"]
    # 起始的url，指的是第一次访问的域名
    start_urls = ["http://www.baidu.com/"]
    #
    def parse(self, response):
        print('理塘顶针')
        pass
