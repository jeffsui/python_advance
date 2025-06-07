import requests

url = "http://httpbin.org"

header = {"token":"201909011313"}

r = requests.get(url+"/get",headers=header)

print(r.text)