#import requests
#
#r = requests.get('https://www.httpbin.org/get')
#print(r.text)


#import  requests
#
#data = {
#    'age':'20',
#    'name':'germey'
#}
#r = requests.get('https://www.httpbin.org/get', params=data)
#print(r.text)


##抓取二进制数据
#import requests
#
#r= requests.get('https://scrape.center/favicon.ico')
#with open('favicon.ico','wb')as f:
#    f.write(r.content)


##添加请求头
#import requests
#
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
#}
#r = requests.get('https://ssr1.scrape.center/',headers=headers)
#print(r.text)


##post请求
#import requests
#
#data = {
#    'name':'germey',
#    'age':'25'
#}
#url = 'https://www.httpbin.org/post'
#r = requests.post(url,data=data)
#print(r.text)


##cookie模拟登录
#import requests
#
#herds = {
#    'Cookie':'_gh_sess=YPOF12Eb0Iyr79WJHRnTw%2F3VX6LSSGyqhRjXNTLiTlLbXOxyOveqMuVsab300trMbfFtnF7kiEJ006rizkPywukIfL5S43P2mDVgHn47sDYHvYiOqbPxmR%2Bv6V3HIpIRTV%2BB0XLG%2F18v0llPD8vSmlB9NXDyv1A5YUfiArBoVmkyckRf%2FA3Ky6H6xtwvPlw9xmarfdAOL80MjB%2BOhIyCaA5V0h8H6llI9L66dUucDyee1mu78ByvMIaDsiUu5sdMAKCBPfAngX92WpnD9XRD5g%2BFMXZp7xv%2Bf5IqfQDF1ZYZY3TQVVq86FKXAmc4al%2FPFqp03oToOJCGI3muPakbWKPPo0rGP1W1pVmjY1cRKjw3uhSlQ3buoQAvxRo4yFchSFu15I09ZrDWYtc6KwE0NrWsQ4kZzjl%2Bwc67keHWJW8oixmPDPAhofE2LVnZT2yCsQ2fK21%2Ftot0nIQWSYY8IiXkHK3Qe9dNxC7cxliAAZVBBJqOj07TmYE7vZkyKyOcKiWvVWnkgKDr%2FypZH8clFbKqmj8rz1zRWsxSfKxT0ReLuOateE%2FUVKLO6nU7HgUYVHV82JsL%2F%2BlnczPBzo4bg0e2KhMhhhadJDxckOhJr9Dl4JY6f04BQg6Ta4ItXIvNjgEvPZMM7LnzscYDd8lzBM%2FzM5mt1KaukLZkvSkBssqoO9LQAT3MXE8jgxPrUwbGoPwaB4crxDrhZ4WEx%2FvW5Nv3GCTeC4rWrQ04w8I5mpUGXFeY2eKQpK4Con3vEcYuDINGlJy9woBb--Gj9THDMOIze%2F5xsR--E6r226ni6x7dcUHmoxCLgg%3D%3D; path=/; secure; HttpOnly; SameSite=Lax'
#}
#r = requests.get('https://github.com/',headers=herds)
#print(r.text)


##
#import requests
#s = requests.session()
#s.get('https://www.httpbin.org/cookies/set/number/123456789')
#r = s.get('https://www.httpbin.org/cookies')
#print(r.text)




