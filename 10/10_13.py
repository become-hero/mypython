import re
rs1=re.match(r"\w{4,10}@(163|qq|outlook)\.com$","python2018@163.com")
print(rs1)
rs2=re.match(r"\w{4,10}@(163|qq|outlook)\.com$","12345@qq.com")
print(rs2)
