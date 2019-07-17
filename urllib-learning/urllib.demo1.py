
from urllib import request

resp = request.urlopen('http://www.baidu.com')
print(resp.readline())
print(resp.getcode())

#urlretrieve函数
request.urlretrieve('http://www.baidu.com/','baidu.html')
request.urlretrieve('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563357876488&di=a01e3f8a3eeb2cf4808ce4c09c2e4d2f&imgtype=0&src=http%3A%2F%2Fpic.9ht.com%2Fup%2F2017-4%2F14910172822196790.jpg', 'DM5.jpg')