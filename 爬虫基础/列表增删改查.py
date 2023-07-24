# # append 末尾添加
# a_list=['aaa','bbb']
# a_list.append('ccc')
# print(a_list)
#
# # insert 指定位置插入
# b_list=['aaa','ccc','ddd']
# # index的值就是想插入位置的下标
# b_list.insert(1,'bbb')
# print(b_list)
#
# # extend 继承  屁股接上
# c_list=[1,2,3]
# d_list=[4,5,6]
# c_list.extend(d_list)
# print(c_list)
#
# print('#########################################')
#
# city_list=['东莞','北京','上海','杭州']
# city_list[2]='东莞'
# # 通过下标修改
# print(city_list)
#
# print('#########################################')
# # 查询
# wantcity=input('输入你生活的城市')
# if wantcity in city_list:
#     print('在')
# else:
#     print('不在')
#
# # not in
#
# if wantcity not in city_list:
#     print('不在')
# else:
#     print('在')

print('#########################################')


# 删除
# del  根据下标删除
g_list=[1,2,3,4,5,6]
# del g_list[2]
# print(g_list)


# pop  直接删除最后一个
# g_list.pop()
# print(g_list)

# remove 根据元素删除

g_list.remove(3)
print(g_list)



