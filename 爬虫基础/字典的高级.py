# # 定义字典
# person = {'name': '吴签', 'age': 28}
#
# # 访问
# print(person['name'])
# print(person['age'])
#
# print(person.get('name'))
# print(person.get('age'))
# # 获取不到？
# print(person.get('sex'))
#
# # 修改
#
# person2 = {'name': '张三', 'age': 28}
#
# person2['name'] = '法外狂徒'
#
# # 增加
# person3 = {'name': '老马', 'age': 24}
# person3['sex'] = '男'
#
# # 删除
# # del
# # 删除指定元素   del person3['age']
# # 删除整个字典  del person3
#
#
# # clear 清空字典 但是存在对象
# # person3.clear()
#
#
# # 遍历
#
person4 = {'name': '丁真', 'age': 19, 'sex': '男'}

# 遍历key
for key in person4.keys():
    print(key)
# #遍历value
for value in person4.values():
    print(value)
# #遍历key 和value
for key, value in person4.items():
    print(key, value)

# 遍历字典的项/元素
for item in person4.items():
    print(item)

