import httpx

url = 'https://spa16.scrape.center/'
client = httpx.Client(http2= True)
r = client.get(url)
print(r.text)