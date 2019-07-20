# 以人人网为例
# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

# 1.不使用cookie去请求大鹏主页
from urllib import request
dapeng_url ='http://www.renren.com/880151247/profile'
# headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#            'Cookie':'anonymid=jyawtp0wadxkfa; depovince=BJ; _r01_=1; jebecookies=80dd94b0-5b59-4714-8a77-c1bbf89ae72a|||||; JSESSIONID=abcAphfrYBgIx91HUpnWw; ick_login=3b75e07f-24be-4890-9d8a-5965d462c82d; _de=7C505DFC8C0E682C4FC4CA2DAE10AAFF1383380866D39FF5; p=c20c0172dc076e2ea8376b3684a409143; first_login_flag=1; ln_uact=liubingqi0001@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn211/20090818/0355/main_IzAB_65590l204235.jpg; t=b33a7838ace6a03369394617f768cbee3; societyguester=b33a7838ace6a03369394617f768cbee3; id=245039683; xnsid=f2bd0c95; ver=7.0; loginfrom=null; jebe_key=e63acb00-1a76-44d4-b3c6-9dfd06c9b383%7C6616409b7bf95ca5e8556a4b0512f71d%7C1563590589114%7C1%7C1563590587456; jebe_key=e63acb00-1a76-44d4-b3c6-9dfd06c9b383%7C6616409b7bf95ca5e8556a4b0512f71d%7C1563590589114%7C1%7C1563590587460; wp_fold=0'}
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))