# Scrapy settings for scrapy_car_038 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_car_038"

SPIDER_MODULES = ["scrapy_car_038.spiders"]
NEWSPIDER_MODULE = "scrapy_car_038.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_car_038 (+http://www.yourdomain.com)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
# 'referer': 'https://www.autohome.com.cn/',
#    'cookie': 'fvlid=1680787976830wLfxua36t8; sessionip=112.93.141.82; sessionid=F0943D62-E1B1-4258-8740-73B3F222CD13%7C%7C2023-04-06+21%3A32%3A58.749%7C%7Cwww.bing.com; autoid=aa28f6f744f83b9514ff00739321a34d; sessionvid=CFAE6BDA-6013-4DD6-8B58-35E4F5A5B088; area=441999; pvidlist=20df9c20-e0ae-42ec-b3b0-375fff75286b22:557829:869147:0:1:4477312; __ah_uuid_ng=c_F0943D62-E1B1-4258-8740-73B3F222CD13; deviceId=F0943D62-E1B1-4258-8740-73B3F222CD13; userCityId=441900; provinceId=440000; cityId=441900; cityName=%u4E1C%u839E; sessionuid=F0943D62-E1B1-4258-8740-73B3F222CD13%7C%7C2023-04-06+21%3A32%3A58.749%7C%7Cwww.bing.com; ahsids=4171_373_66; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1680788188; ahpvno=11; pvidchain=6841395,3311667,3311667,104399,104400,104399,3311664,3311273,3311273,3311273; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1680788204; v_no=11; visit_info_ad=F0943D62-E1B1-4258-8740-73B3F222CD13||CFAE6BDA-6013-4DD6-8B58-35E4F5A5B088||-1||-1||11; ref=www.bing.com%7C0%7C0%7C0%7C2023-04-06+21%3A36%3A46.896%7C2023-04-06+21%3A32%3A58.749'
# # }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapy_car_038.middlewares.ScrapyCar038SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_car_038.middlewares.ScrapyCar038DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_car_038.pipelines.ScrapyCar038Pipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
