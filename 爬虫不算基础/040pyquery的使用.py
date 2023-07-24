# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# # print(doc('li'))
# print(doc('#container .list li'))
# print(type(doc('#container.list li')))
#
# for item in doc('#container .list li').items():
#     print(item.text())


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
# items = doc('.list')
# container = items.parents()
# print(type(container))
# print(container)


# li = doc('.list .item-0.active')
# print(li.siblings())


# attr方法获取属性
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)
