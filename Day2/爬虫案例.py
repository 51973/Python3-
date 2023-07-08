import requests
import logging
import re
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10


def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status_code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,
                      exc_info=True)

def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern,html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL,item)
        logging.info('get detail url %s', detail_url)
        yield detail_url

def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):

    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None

    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>',re.S)
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []

    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>',re.S)
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    return {
        'name':name,
        'categories':categories,
        'drama':drama
    }

def main(page):
    #总页数 原来url+page
    index_html = scrape_index(page)
    #获取详情url
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        #解析详情页
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        #打印
        logging.info('get detail data %s', data)
        logging.info('saving data to json file')
        logging.info('data saved successfully')

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()