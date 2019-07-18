
from urllib import request

#ulopen函数的用法
#resp = request.urlopen('http://www.baidu.com')
#print(resp.readline())
#print(resp.getcode())

#urlretrieve函数
#request.urlretrieve('http://www.baidu.com/','baidu.html')
#request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563357876488&di=a01e3f8a3eeb2cf4808ce4c09c2e4d2f&imgtype=0&src=http%3A%2F%2Fpic.9ht.com%2Fup%2F2017-4%2F14910172822196790.jpg', 'DM5.jpg')


#ulencode函数用法  parse_qs函数解码 将字典转变成格式化后的字符串
# from urllib import parse
# data = {'name':'爬虫基础','greet':'hello world','age':100}
# qs = parse.urlencode(data)
# print(qs)
# from urllib import request
# from urllib import parse
# url = 'http://www.baidu.com/s'
# params = {'wd':'刘德华'}
# qs = parse.urlencode(params)
# url = url + '?' + qs
# resp = request.urlopen(url)
# print(resp.read())

from urllib import request
from urllib import parse
params = {'wd':'刘德华'}
qs = parse.urlencode(params)
result = parse.parse_qs(qs)
print(result)