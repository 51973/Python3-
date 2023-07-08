#from lxml import etree
#text = '''
#<div>
#    <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a>
#     </ul>
# </div>
#'''
#html = etree.HTML(text)
#result = etree.tostring(html)   # 最后一个<li>没有闭合，etree模块自动修复，tostring即可输出修正HTML代码
#print(result.decode('utf-8'))



##也可以不声明
#from lxml import etree
#
#html = etree.parse('./test.html',etree.HTMLParser())
#result = etree.tostring(html)
#print(result.decode('utf-8'))


##所有节点
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//*')
# print(result)

##所有li标签
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li')
# print(result)
# print(result[0])



##子节点
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

##父节点
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//a[@href="link2.html"]/../@class')
# print(result)


##文本获取
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/a/text()')
# print(result)


##属性获取
# from lxml import etree
# html = etree.parse('./test.html',etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# print(result)



##属性多值匹配
# from lxml import etree
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class, "li")]/a/text()')
# print(result)



##节点轴选择
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')
print(result)



