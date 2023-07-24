# # # 序列化
# fp = open('test1.txt', 'w')
# # fp.write('hello world')
# # # 默认情况下只能将字符串写入到文件
# fp.close()
# #
# name_list=['zhangsan','lisi']
# # # 无法写入 write() argument must be str, not list
# # # fp.write(name_list)
# #
# # # 序列化的两种方式
# # # dumps()
# # fp = open('test2.txt', 'w')
# # # 创建列表
# # name_list = ['zhangsan', 'lisi']
# # # 导入json模块到该文件
# # import json
# #
# # # 将对象变成json字符串
# # # names=json.dumps(name_list)
# # #
# # # print(names)
# # # print(type(names))
# # #
# # # fp.write(names)
# # # fp.close()
# #
# # # dump
# # # 转换为字符串的同时，指定一个对象的文件，把转换后的字符串写入到这个文件里面
# # namee_list = ['zs', 'ls']
# # json.dump(namee_list, fp)
# # # fp.close()
#
# # # 反序列化
# # import json
# #
# # fp = open('test.txt', 'w')
# # fp.write("helloworld")
# # fp = open('test.txt', 'r')
# #
# # # loads
# # content = fp.read()
# # result = json.loads(content)
# # print(result)
#
#
# # load
# fp=open('test.txt','r')
# import  json
# result=json.load(fp)
# print(result)
#
