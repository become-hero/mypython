import urllib.request
response=urllib.request.urlopen("http://www.baidu.com")
print(response.status)
print("headers:",response.getheaders())
print("header date:",response.getheader("Date"))
