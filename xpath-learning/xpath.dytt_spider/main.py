from lxml import etree
import requests
BASE_DOMAIN = 'http://dytt8.net'

url = 'https://dytt8.net/html/gndy/dyzz/list_23_1.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
response = requests.get(url,headers=headers)
# print(response.text)
# 注意此处涉及上一讲中提到的text和content的区别，所以直接用text打印会出现筹码
# requests库，为谁会使用自己猜测的编码方式，将抓取下来的网页进行解码，然后存储到text属性上
# 在电影天堂地的网页中，因为编码方式，requests库猜错了，所以就会产生乱码
# print(response.content.decode('gbk'))   #查询编码方式见笔记，此处是可以正确打印出来的
text = response.content.decode('gbk')
html = etree.HTML(text)
detail_urls =  html.xpath("//table[@class = 'tbspan']//a/@href")
for detail_url in detail_urls:
    print(BASE_DOMAIN + detail_url)