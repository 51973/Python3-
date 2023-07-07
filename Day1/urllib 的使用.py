#import urllib.request
#reponse = urllib.request.urlopen('https://www.python.org/')
#print(reponse.status)       # 响应状态码
#print(reponse.getheaders)
#print(reponse.getheader('Server'))         # 获取服务器用什么搭建的
#print(type(reponse))          # 输出响应类型
#print(reponse.read().decode('utf-8'))

##  data 参数
#import urllib.parse
#import urllib.request

#data = bytes(urllib.parse.urlencode({'name':'germey'}),encoding='utf-8')
#resp = urllib.request.urlopen('https://www.httpbin.org/post',data=data)
#print(resp.read().decode('utf-8'))


##timeout参数
#import socket
#import urllib.request
#import urllib.error

#try:
#    resp = urllib.request.urlopen('https://www.httpbin.org/get',timeout=0.1)
#except urllib.error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print('Time out')


##Request
#import urllib.request

#request = urllib.request.Request('https://www.python.org/')
#resp = urllib.request.urlopen(request)
#print(resp.read().decode('utf-8'))


##高级用法
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
passworld = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username,passworld)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
