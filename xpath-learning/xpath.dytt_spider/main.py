from lxml import etree
import requests
BASE_DOMAIN = 'http://dytt8.net'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }


def get_detail_urls(url):
    # url = 'https://dytt8.net/html/gndy/dyzz/list_23_1.html'

    response = requests.get(url, headers=HEADERS)
    # print(response.text)
    # 注意此处涉及上一讲中提到的text和content的区别，所以直接用text打印会出现筹码
    # requests库，为谁会使用自己猜测的编码方式，将抓取下来的网页进行解码，然后存储到text属性上
    # 在电影天堂地的网页中，因为编码方式，requests库猜错了，所以就会产生乱码
    # print(response.content.decode('gbk'))   #查询编码方式见笔记，此处是可以正确打印出来的
    # print(response.encoding)     #此代码用于查看默认的编码方式

    # text = response.content.decode('gbk')
    text = response.text
    # text = response.text.encode().decode()
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class = 'tbspan']//a/@href")
    #以下的map函数等价于以下注释的代码
    # def abc(url):
    #     return BASE_DOMAIN+url
    # index = 0
    # for detail_url in detail_urls:
    #     detail_url=abc(detail_url)
    #     detail_urls[index]=detail_url
    #     index += 1

    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

    # for detail_url in detail_urls:
    #     print(BASE_DOMAIN + detail_url)

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    # print(title)
    # for x in title:
    #     print(etree.tostring(x,encoding='utf-8').decode('utf-8'))
    movie['title']=title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover']=cover
    movie['screenshot']=screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    # print(infos)
    for index,info in enumerate(infos):
        # print(info)
        # print(index)
        # print('-'*30)
        if info.startswith("◎年　　代"):
            # info = info.replace("◎年　　代","").strip()
            # print(info)
            info = parse_info(info,"◎年　　代")
            movie['year']=info
        elif info.startswith("◎产　　地"):
            # info = info.replace("◎产　　地","").strip()
            info = parse_info(info, "◎产　　地")
            movie['country']=info
        elif info.startswith("◎类　　别"):
            info = parse_info(info, "◎类　　别")
            movie['catagory']=info
        elif info.startswith("◎豆瓣评分"):
            info = parse_info(info, "◎豆瓣评分")
            movie['douban_rating'] = info
        elif info.startswith("◎片　　长"):
            info = parse_info(info, "◎片　　长")
            movie['duration'] = info
        elif info.startswith("◎导　　演"):
            info = parse_info(info, "◎导　　演")
            movie['director'] = info
        elif info.startswith("◎主　　演"):
            info = parse_info(info, "◎主　　演")
            for x in range(index+1,100):
                pass




def spider():
    base_url = 'https://dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1,8):
        # 第一个for循环用来控制总共有7页
        print('x'*30)
        print(x)
        print('x'*30)
        url = base_url.format(x)
        # print(url)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            #第二个for循环用来遍历一页中所有电影的详情url
            movie = parse_detail_page(detail_url)
            break

if __name__ == '__main__':
    spider()