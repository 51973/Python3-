import requests
import logging

INDEX_URL = 'https://spa1.scrape.center/api/movie?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

LIMT = 10
#https://spa1.scrape.center/api/movie?limit=10&offset=0
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMT, offset=LIMT*(page-1))
    return scrape_api(url)

DETATL_URL = 'https://spa1.scrape.center/api/movie/{id}'
def scrape_detail(id):
    url = DETATL_URL.format(id=id)
    return scrape_api(url)

TOTAL_PAGE = 10
def main():
    for page in range(1, TOTAL_PAGE + 1):
        index_data = scrape_index(page)
        for item in index_data.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            detail_data.pop('photos')  # 删除photos键及其对应的值
            detail_data.pop('actors')  # 删除image键及其对应的值
            detail_data.pop('directors')
            print(detail_data)  # 打印剩余的数据


if __name__ == '__main__':
    main()
