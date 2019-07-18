from urllib import request,parse

url = 'https://music.163.com/weapi/search/suggest/web?csrf_token='
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
formdata={
    'params':'5wm2DqbhSVUq+E2ZCvgA0A9n0K+onm6zdJXq6bPYiqxzMnqNW/Dhf5pZ3ReFMrggSUqAft7AJkeLgMi/PJTgEKofkDqiZDnrZIzNDs/5Bt0=',
    'encSecKey':'3e67eae77514e4cede64e516e97ec2b06e0773363f76519f2c9fc2952658ae958c787fd0629892f45b86a10f51400e87e131ac7fa44cf2bd29ec19b6c1c62d06220b803d05bed8f8597ca759ca2006b6b95f3a229f5dd6ced0e46ef7e89fe0ccc871b56a064d7f2c1dc94c3f2548be05ed8aa0718303d8022c6ea5989dcf6ae7'
}
req = request.Request(url=url,headers=headers,data=parse.urlencode(formdata).encode('utf-8'))
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))