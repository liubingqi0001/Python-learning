from urllib import request
from http.cookiejar import MozillaCookieJar

#保存百度的cookie信息
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
#
# resp = opener.open('http://www.baidu.com/')
#
# cookiejar.save()

#保存httpbin.org的cookie信息
# cookiejar = MozillaCookieJar('cookie.txt')
# handler = request.HTTPCookieProcessor(cookiejar)
# opener = request.build_opener(handler)
#
# resp = opener.open('http://httpbin.org/cookies/set/course/spider')
#
# cookiejar.save(ignore_discard=True)

#从本地读取并仁慈cookie
cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies/set/course/spider')

for cookie in cookiejar:
    print(cookie)
#cookiejar.save(ignore_discard=True)