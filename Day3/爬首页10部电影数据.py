import requests
from pyquery import PyQuery as pq
import re

url = 'https://ssr1.scrape.center/'
html = requests.get(url).text
doc = pq(html)
#遍历
items = doc('.el-card').items()
file = open('moies.txt','w',encoding='utf-8')

for item in items:

    name = item('a>h2').text()
    file.write(f'名称:{name}\n')

    cat = [item.text()for item in item.find('.categories button span').items()]
    file.write(f'类型:{cat}\n')

    pub = item.find('.info:contains(上映)').text()
    pub = re.search('(\d{4}-\d{2}-\d{2})',pub).group(1)\
    if pub and re.search('\d{4}-\d{2}-\d{2}',pub) else None
    file.write(f'上映时间:{pub}\n')
file.close()