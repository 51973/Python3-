import requests

resp = requests.get('https://ssr2.scrape.center/',verify=False)
print(resp.status_code)