# 创建文件
# 模式： w,可写
#       r,可读
#       a，追加

# open('test.txt', 'w')
#  打开
# fp = open('test.txt', 'w')
# fp.write('hello world')
#
# f1 = open('demo/test1.txt','w')
#
# # 文件的关闭
# fp.close()
# f1.close()

#文件的读写
fp = open('test.txt', 'w')
fp.write('hello world\n'*5)
fp.close()
# 如果再运行一次，是覆盖还是写10次？？     覆盖
# 如果文件存在，会清空再写
# 如果想追加用a模式(append)

fp=open('test.txt','r')
content =fp.read()
# content =fp.readline() 只能读一行
# content =fp.readlines() 读多行，变成列表
print(content)






