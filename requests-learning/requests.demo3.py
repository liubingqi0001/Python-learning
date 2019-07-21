import requests

proxy = {
    'http':'123.207.66.220:1080',
    'https':'123.207.66.220:1080'
}


response = requests.get('http://httpbin.org/ip',proxies=proxy)
print(response.text)