import scrapy
import json


class TestpostSpider(scrapy.Spider):
    name = "testpost"
    allowed_domains = ["https://fanyi.baidu.com/sug/"]

    # post请求如果没有参数，那么就没意义
    # 所以parse方法也没有意义
    # start_urls = ["http://fanyi.baidu.com/"]

    # def parse(self, response):
    #     pass\

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content, encoding='utf-8')

        print(obj)
