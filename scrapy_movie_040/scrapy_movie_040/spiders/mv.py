import scrapy

from scrapy_movie_040.scrapy_movie_040.items import ScrapyMovie040Item


class MvSpider(scrapy.Spider):
    name = "mv"
    allowed_domains = ["dydytt.net"]
    start_urls = ["http://dydytt.net/"]

    def parse(self, response):
        print('=================')
        # 第一页的名字和第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            # 获取第一页的name和要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'https://www.dytt8.net' + href
            print(url)

            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # # 注意 如果拿不到数据的情况下
        # 一定检查你的xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # print('src')
        # 接受到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovie040Item(src=src, name=name)
        yield movie
        pass
