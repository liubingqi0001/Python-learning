from urllib import request

url ='http://httpbin.org/ip'

#没有使用代理的返回值
# resp = request.urlopen(url)
# print(resp.read())

#使用了代理的返回值
#1、使用ProxyHandler传入代理构建一个handler
handler = request.ProxyHandler({"http":"121.13.252.62:41564"})
#或者可以两个参数都写上，如下
# handler = request.ProxyHandler({"http":"121.13.252.62:41564",
#                                 "https":"121.13.252.62:41564"})

#2、使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
#3、使用opener去发送一个请求
resp = opener.open(url)
print(resp.read())