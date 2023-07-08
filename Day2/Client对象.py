import httpx

with httpx.Client() as client:
    resp = client.get('https://www.httpbin.org/get')
    print(resp)