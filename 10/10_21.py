import re
infos="Tom:13800000000,David:13600000000"
iter_obj=re.finditer(r"1[3578]\d{9}",infos)
for iter in iter_obj:
    print(iter.group())
