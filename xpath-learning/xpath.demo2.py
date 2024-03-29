from lxml import etree

# 1. 获取所有tr标签
# 2. 获取第二个tr标签
# 3. 获取所有class等于even的tr标签
# 4. 获取所有a标签的href属性
# 5. 获取所有的职位信息（纯文本）

parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse('tencent.html',parser = parser)

# 1. 获取所有tr标签
# //tr   即为xpath代码
# xpath函数返回的是一个列表，所以在后面打印时用tostring，然后编码，解码
# trs = html.xpath('//tr')
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 2. 获取第二个tr标签
# 下面第一个语句，写个[0]表示取出第一个元素，即tr；若没有[0]，则返回的是trs，需要像上面一样用for来打印
# tr = html.xpath('//tr[2]')[0]
# print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 3. 获取所有class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode('utf-8'))

# 4. 获取所有a标签的href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print('http://hr.tencent.com/'+a)

# 5. 获取所有的职位信息（纯文本）
# 两步：第一步获取所有tr标签，第二步获取所有tr标签的值
trs = html.xpath('//tr[position()>1]')
positions = []
for tr in trs:
    # 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素，应该在//之前加一个点，代表是在当前元素下获取
    href = tr.xpath('.//a/@href')[0]
    fullurl = 'http://hr.tencent.com/' +href
    #title = tr.xpath('.//a/text()')[0]
    title = tr.xpath('./td[1]//text()')[0]
    catagory = tr.xpath('./td[2]/text()')[0]
    nums = tr.xpath('./td[3]/text()')[0]
    address= tr.xpath('./td[4]/text()')[0]
    publishtime = tr.xpath('./td[5]/text()')[0]

    position = {
        'url': fullurl,
        'title':title,
        'catagory':catagory,
        'nums':nums,
        'address':address,
        'publishtime':publishtime
    }
    positions.append(position)

print(positions)

