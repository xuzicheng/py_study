import jsonpath
import json

#  https://blog.csdn.net/luxideyao/article/details/77802389学习链接

obj = json.load(open('文件名', 'r', encoding='utf-8'))

# 书店所有书的作者
# author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')

# 所有的作者
# author_list = jsonpath.jsonpath(obj,'$..author')

# store下面的所有的元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')

# store里面所有东西的price
price_list = jsonpath.jsonpath(obj, '$.store..price')

# 最后一本书
book1 = jsonpath.jsonpath(obj, '$..book[(@.length-1])')

# 前面的两本书
book1 = jsonpath.jsonpath(obj, '$..book[0,1])')
book2 = jsonpath.jsonpath(obj, '$..book[:2])')

# 条件过滤格式要加？
# 过滤出所有的包含isbn的书
book3 = jsonpath.jsonpath(obj, '$..book[(?@.isbn)]')

# 哪本书超过10块
book_list = jsonpath.jsonpath(obj, '$..book[(?@.price>10)]')


