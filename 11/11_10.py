import requests
data={
    "key":"python",
    "page":10
}
response=requests.get("http://httpbin.org/get",params=data)
#response=requests.get("http://httpbin.org/get?key=python&page=10")
print("url: {}".format(response.url))
print("tmp:  \n",response.text)
