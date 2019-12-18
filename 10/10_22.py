import re
stu="Tom 13800000000 Male"
stu_new=re.sub("\s",",",stu)
print("stu={}".format(stu))
print("stu_new={}".format(stu_new))
