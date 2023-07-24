# try:
#     可能出现的代码
# except 异常类型
#     友好地提示
#

try:
    fp=open('ttt.txt','r')
    fp.read()
except FileNotFoundError:
    print('找不到啊')