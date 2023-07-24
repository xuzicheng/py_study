age=input('输入你的年龄')
print(type(age))#说明返回的是str类型
if int(age)>18:
    print('可以去网吧')
    print('233')#可以多行if
else:
    print('不给去网吧')

score=89

if score>=90:
    print('666')
elif score>=80:
    print('555')