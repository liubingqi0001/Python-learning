import requests

data = {
    'first':'true',
    'pn':1,
    'kd':'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie':'JSESSIONID=ABAAABAAAIAACBI4C64DECADF0866CED8C6EE8CD9C40045; _ga=GA1.2.178634616.1563717563; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563717563; user_trace_token=20190721215923-beb80289-abbf-11e9-a4eb-5254005c3644; LGSID=20190721215923-beb80635-abbf-11e9-a4eb-5254005c3644; LGUID=20190721215923-beb8094c-abbf-11e9-a4eb-5254005c3644; _gid=GA1.2.1650773390.1563717563; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; X_HTTP_TOKEN=eb3006fd6e18baa07188173651d9678d2202390703; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1563718817; LGRID=20190721222017-aa15c161-abc2-11e9-813e-525400f775ce; SEARCH_ID=78624672a3d7461493885a5b3d9af9b9',
    'Origin':'https://www.lagou.com'
    }
response =requests.post("https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false",data=data,headers=headers)
print(response.text)

#代码运行爬取失败，原因不明，应该是拉勾的反爬虫技术太牛