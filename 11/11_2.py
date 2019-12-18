import urllib.request
import urllib.parse
param_dict={"key":"hello"}
param_str=urllib.parse.urlencode(param_dict)
param_datas=bytes(param_str,encoding="utf-8")
response=urllib.request.urlopen("http://httpbin.org/post",data=param_datas)
print(response.read())
