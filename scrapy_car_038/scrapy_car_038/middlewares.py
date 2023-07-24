# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class ScrapyCar038SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapyCar038DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # request.cookies = {
        #     'cookie': 'fvlid=1680787976830wLfxua36t8; sessionip=112.93.141.82; sessionid=F0943D62-E1B1-4258-8740-73B3F222CD13%7C%7C2023-04-06+21%3A32%3A58.749%7C%7Cwww.bing.com; autoid=aa28f6f744f83b9514ff00739321a34d; sessionvid=CFAE6BDA-6013-4DD6-8B58-35E4F5A5B088; area=441999; pvidlist=20df9c20-e0ae-42ec-b3b0-375fff75286b22:557829:869147:0:1:4477312; __ah_uuid_ng=c_F0943D62-E1B1-4258-8740-73B3F222CD13; deviceId=F0943D62-E1B1-4258-8740-73B3F222CD13; userCityId=441900; provinceId=440000; cityId=441900; cityName=%u4E1C%u839E; sessionuid=F0943D62-E1B1-4258-8740-73B3F222CD13%7C%7C2023-04-06+21%3A32%3A58.749%7C%7Cwww.bing.com; ahsids=4171_373_66; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1680788188; ahpvno=11; pvidchain=6841395,3311667,3311667,104399,104400,104399,3311664,3311273,3311273,3311273; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1680788204; v_no=11; visit_info_ad=F0943D62-E1B1-4258-8740-73B3F222CD13||CFAE6BDA-6013-4DD6-8B58-35E4F5A5B088||-1||-1||11; ref=www.bing.com%7C0%7C0%7C0%7C2023-04-06+21%3A36%3A46.896%7C2023-04-06+21%3A32%3A58.749',
        #     'referer': 'https://www.autohome.com.cn/'
        # }
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
