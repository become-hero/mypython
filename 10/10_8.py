import re
def reg_phone(phone):
    rs=re.match("1[3578]\d{9}",phone)
    if rs==None:
        return False
    else:
        print(rs.group())
        return True
#test1
print("test1------------------")
print(reg_phone("13688888888"))
#test2
print("test2---------------")
print(reg_phone("14688888888"))
#test3
print("test3------------------")
print(reg_phone("13677777777abc"))
