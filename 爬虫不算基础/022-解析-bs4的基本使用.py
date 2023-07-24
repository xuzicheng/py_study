from bs4 import BeautifulSoup

# 解析本地文件
# 點认打开的文件的编码格式是gbk 所以在打开文件的时需要指定编码
soup = BeautifulSoup(open('022-解析-bs4的基本使用.html', encoding='utf-8'), 'lxml')
# print(soup)

# 根据标签名查找节点
# 找到的第一个符合条件的数据
# print(soup.a)

# 获取标签的属性值
# print(soup.a.attrs)

# bs4的函数
# (1)find 返回第一个符合条件的数据
# print(soup.find('a'))
# print(soup.find('a',title="a2 "))
# 根据class的值找到对象，注意class需要添加下划线
# print(soup.find('a',class_="a1"))


# (2)find_all  返回列表 所有的a标签
# print(soup.findAll('a'))
# 如果想要获取多个标签数据，要把他们放在[]列表里面
# print(soup.findAll(['a','span']))
# limit限制查找前几个
# print(soup.findAll('li',limit=2))


# (3)select 推荐
# print(soup.select('a'))
# # 可以通过.代表class，我们称之为类选择器
# print(soup.select('a1'))
# print(soup.select('#l1'))

# 属性选择器--通过属性查找对应标签
# 查找li标签里面有id的标签
# print(soup.select('li[id]'))

# 层级选择器
# 1：后代选择器
#   找到div下面的li
# print(soup.select('div li'))

# 2:子代选择器
# print(soup.select('div > ul > li'))

# 找到a标签和li标签所有对象
# print(soup.select('a,li'))

# 节点信息模块
# 获取节点内容
# obj = soup.select('#d1')[0]
# # 如果标签对象中 只有内容的话那么下面两个方法都可用
# # 如果标签对象中 除了内容还有标签，那么string无法获取数据
# # 一般情况下，推荐使用get_text
# print(obj.string)
# print(obj.get_text())

# 节点的属性
obj=soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为字典返回
# print(obj.attrs)

# 获取节点的属性
# print(obj.attrs.get('class'))
# print(obj.get('class'))
# print(obj['class'])


