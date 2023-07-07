from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
Proxy_Handler = ProxyHandler({
    'http':'http://124.221.147.228:443'
})
opner = build_opener(Proxy_Handler)
try:
    reso = opner.open('http://www.baidu.com')
    print(reso.read().decode('utf-8'))
except URLError as e:
    print(e.reason)