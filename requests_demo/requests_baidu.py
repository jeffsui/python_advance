import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3878.400 QQBrowser/10.8.4518.400'}

data={
    "wd":'python'
}
resp = requests.get("https://www.baidu.com/s",params=data,headers=headers)
resp.encoding = 'utf-8'
print(resp.text)

