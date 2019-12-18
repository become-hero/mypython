import urllib.request
import urllib.parse
url="http://httpbin.org/post"
headers={"User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
data_dict={"word":"hello world"}
data=bytes(urllib.parse.urlencode(data_dict),encoding="utf8")
request_obj=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response=urllib.request.urlopen(request_obj)
print(response.read().decode("utf8"))
