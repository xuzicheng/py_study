import re

line = "boooooooooooaaaaaaaaaaooooobbbacby123"
# ^开头
# *	匹配前⼀个字符出现0次或者⽆限次，即可有可⽆
# $ 结尾字符
# 3$ 以3结尾
# regex_str="^b.*"
# ? 从左往右匹配，非贪婪
# regex_str = '.*?(b.*?b).*'
# {m}	匹配前⼀个字符出现m次	用在字符或(...)之后	ab{2}c	abbc
# [ ]	匹配[ ]中列举的字符 满足任意一个就行
# |	匹配左右任意⼀个表达式 a|b
regex_str =".*(b.{2,4}b)."
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))
