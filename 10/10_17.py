import re
pattern=re.compile("\w{4,10}@163\.com$")
rs=re.match(pattern,"python2018@163.com")
print(rs)
rs=re.match(pattern,"vip_python@163.com")
print(rs)
rs=re.match(pattern,"abc@163.com")
print(rs)
