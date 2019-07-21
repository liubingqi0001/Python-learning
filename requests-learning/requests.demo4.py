import requests

# 以下代码为获取cookie的方法
# respons = requests.get('https://www.baidu.com/')
# print(respons.cookies)
# print(respons.cookies.get_dict())

# 以下代码为通过session共享cookie
url = "http://www.renren.com/PLogin.do"
data = {"email":"970138074@qq.com",'password':"pythonspider"}
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
session = requests.session()

session.post(url,data=data,headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(response.text)
