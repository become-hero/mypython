import re
infos="Tom:python_vip@163.com,David:12345@qq.com"
list=re.findall(r"(\w{3,20}@(163|qq)\.com)",infos)
print(list)
