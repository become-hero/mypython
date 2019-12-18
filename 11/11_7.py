import urllib.request
import urllib.parse
import urllib.error
url="http://www.hhhhhddddd123.com"
'''
try:
    request_obj=urllib.request.Request(url=url)
    response=urllib.request.urlopen(request_obj)
except urllib.error.URLError as e:
    print(e.reason)
'''
try:
    responese=urllib.request.urlopen("http://www.doban.com/abc")
except urllib.error.HTTPError as e:
    print("发现HTTPError异常，异常原因：",e.reason)
    print("响应状态码：",e.code)
    print("请求头信息：",e.headers)
except urllib.error.URLError as err:
    print(err.reason)

