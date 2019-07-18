from urllib import request,parse

# url = 'https://www.qiushibaike.com/text/'
# headers = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# req = request.Request(url=url,headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))

#官方给的作业代码
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Referer": "https://www.qiushibaike.com/text/",
    "Origin": "https://www.qiushibaike.com"
}
req = request.Request("https://www.qiushibaike.com/text/page/2/",headers=headers)
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))