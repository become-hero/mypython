import re
def reg_phone(phone):
    rs=re.match("1[3578]\d{9}$",phone)
    if rs==None:
        return False
    else:
        print(rs.group())
        return True
print("test1----------------")
print(reg_phone("13600000000"))
print("test2----------------")
print(reg_phone("14600000000"))
print("test3----------------")
print(reg_phone("13600000000abc"))
