import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["https://cn.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=uuid_906861ad21fc45e19c0ab61cc594ade2%2Cclassify_B&search_uuid=906861ad21fc45e19c0ab61cc594ade2"]
    start_urls = ["https://cn.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=uuid_906861ad21fc45e19c0ab61cc594ade2%2Cclassify_B&search_uuid=906861ad21fc45e19c0ab61cc594ade2/"]

    def parse(self, response):
        # conetent =response.text
        # content =response.body
        # print('============================')
        # print(conetent)
        span=response.xpath('//*[@id="filter"]/div[1]/a[1]/span')[0]
        print('============================')
        print(span.extract())

        pass
