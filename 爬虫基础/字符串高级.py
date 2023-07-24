# len  获取长度
s = 'china'
print(len(s))

# find 查找内容  返回第一次出现的下标
s1 = 'chinac'
print(s1.find('c'))

# 判断startswith endswith  判断是不是以谁谁谁开头或结尾
print(s.startswith('c'))
print(s.endswith('a'))

# count 计算出现的次数
s3 = 'aaaabbbb'
print(s3.count('a'))

# replace  替换字符串
s4 = 'ccddd'
print(s4.replace('c', 'e'))

# spilt 切割字符串
s5 = '1#3#4#4#5'
print(s5.split('#'))

# strip 去除空格
s9 = '    c    '
print(len(s9.strip()))
