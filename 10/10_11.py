import re
rs=re.match("\w{4,10}@163\.com$","python3018@163.com")
print(rs)
rs=re.match("\w{4,10}@163.com$","abc@163.com")
print(rs)
rs=re.match("\w{4,10}@163.com$","vip_python32018@163.com")
print(rs)
