# 爬虫分两部分

import requests
from lxml import etree

# 1.将目标网站上的页面抓取下来
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Referer':'https://www.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/beijing/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)
# response.text 返回的是经过解码后的字符串，是str(unicode)类型
# response.content 返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理的字符串，是bytes类型

# 2.将抓取下来的数据根据一定的规则进行提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode('utf-8'))
# 接下来通过ul 获取所有的li
lis = ul.xpath("./li")
movies = []
for li in lis:
    # print(etree.tostring(li,encoding='utf-8').decode('utf-8'))
    title = li.xpath("@data-title")[0]
    score = li.xpath('@data-score')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title':title,
        'score':score,
        'duration':duration,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)

print(movies)