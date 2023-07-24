# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


# 如果想使用管道的话，那么必须在setting中开启管道
class ScrapyDangdang039Pipeline:
    # item就是yield后面的book对象
    # 执行前用的方法
    def open_spider(self, spider):
        print('++++++++++++++++++++++')
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 以下这种模式不推荐 因为每传送过来一个对象 那么就打开一次文件 对文件的操作过于频樂
        # write() argument must be str, not ScrapyDangdang039Item
        # write方法必须要写一个字符串，不能是对象
        # w模式会每个对象都打开一个文件，覆盖之前内容然后关闭
        #
        # with open('book.json','a',encoding='utf-8')as fp:
        #     fp.write(str(item))

        self.fp.write(str(item))
        return item

    # 在爬虫文件执行完之后 执行的方法
    def close_spider(self, spider):
        print('----------------------------')
        self.fp.close()


# 多条管道同时下载
# 1:定义管道类
# 2:setting开启管道  "scrapy_dangdang_039.pipelines.DangdangDownload":301
import urllib.request


class DangdangDownload:
    def process_item(self, item, spider):
        # urllib.request.urlretrieve(url=url,filename=filename)
        url = 'http:' + item.get('src')
        filename = './book/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item


# 加载setting
from scrapy.utils.project import get_project_settings
import pymysql


class mysqlpipeline:
    def open_spider(self, spider):
        settings = get_project_settings()
        # db_host = '127.0.0.1'
        # db_port = 3306
        # db_user = 'root'
        # db_password = 'zse123579'
        # db_name = 'python_dangdang'
        # db_charset = 'utf-8'
        self.host = settings['db_host']
        self.port = settings['db_port']
        self.user = settings['db_user']
        self.password = settings['db_password']
        self.name = settings['db_name']
        self.charset = settings['db_charset']


        self.connect()

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into book(name,src) values ("{}","{}")'.format(item['name'], item['src'])
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交sql语句
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
