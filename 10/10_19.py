import re
infos="Tom:13300000000,David:13800000000"
list=re.findall(r"1[3578]\d{9}",infos)
print(list)
