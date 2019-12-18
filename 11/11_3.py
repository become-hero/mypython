import urllib.request
response=urllib.request.urlopen("http://www.baidu.com",timeout=0.001)
print(response.read())
