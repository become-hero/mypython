import re
def reg_identifier(str):
    rs=re.match("^[0-9]\w*",str)
    if rs!=None:
        return False
    else:
        return True
print("1_name--->是否合法：{}".format(reg_identifier("1_name")))
print("name_1--->是否合法：{}".format(reg_identifier("name_1")))
