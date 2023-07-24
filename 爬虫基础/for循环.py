# s='china'
# for i in s:
#     # i是字符串中一个又一个字符变量
#     # s是要遍历的数据
#     print(i)


# range(1,6)
# range(起始值，结束值) 左闭右开
for i in range(1, 6):
    print(i)
print('###############')
# range（1，10，3）(3是步长的意思)
for b in range(1, 10, 3):
    print(b)
print('###############')

a_list = ['aa', 'bb', 'cc']
for c in a_list:
    print(c)

    print('###############')

    # 遍历列表下标
    print(len(a_list))  # 判断个数
    for d in range(len(a_list)):
        print(d)
