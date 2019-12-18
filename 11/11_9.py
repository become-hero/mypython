import requests
response=requests.get("http://httpbin.org/get")
print("type: {}".format(type(response)))
print("status_code: {}".format(response.status_code) )
print(response.text)
