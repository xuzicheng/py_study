from lxml import etree

# xpath解析
# （1)本地文件                                         etree.parse()
#  (2)服务器响应的数据response.read().decode('utf-8)    etree.HTML()

tree = etree.parse('017-解析-xpath基本使用.html')

# print(tree)


# //:查找所有子孙节点，不考虑层级关系
# /:找直接子节点

# tree.xpath('xpath路径')  查找ul下面的li
# li_list = tree.xpath('//body/ul/li')
# # 判断列表长度
# print(len(li_list))
# print(li_list)


# 查找所有有id的厲性的1i标签
# text() 获取标签内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l1的标签  注意""的问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# 查找到id为l1的l1标签的ClaSS的属性值
# li_list=tree.xpath('//ul/li[@id="l1"]/@class')

# 查询id中包含l的li标签
# li_list=tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查询id的值以l开头的1i标签
# li_list=tree.xpath('//ul/li[starts-with(@id,"l")]/text()')


print(li_list)
print(len(li_list))
