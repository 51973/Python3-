# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))


##URL 初始化
# from pyquery import PyQuery as pq
# doc = pq(url='https://cuiqingcai.com/')
# print(doc('title'))


##基本css选择器
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
# doc = pq(html)
#
# #属性下的list标签的所有li
# #print(doc('#container .list li'))
# print(type(doc('#container .list li')))
#
#
# for item in doc('#container .list li').items():
#     print(item.text())


##查找节点
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print('父节点')
# print(items.parent())
# print('子节点')
# print(items.children())
# print('兄弟节点')
# items = doc('.list .item-0.active')
# print(items.siblings())
#
# print(items.siblings('.active'))
# print('获取属性')
# a = doc('.item-0.active a')
# ##attr获取属性
# print(a.attr('href'))
#
# print('获取文本')
# a = doc('.item-0.active a')
# print(a.text())


##remove
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
##移除p
wrap.find('p').remove()
print(wrap.text())