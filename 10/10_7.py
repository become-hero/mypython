import re
user_info=["Tom,13812345678,20","David,,30","Lilei,18851888888,25"]
for user in user_info:
    rs=re.match("\w+,[0-9]{11},\d+",user)
    if rs!=None:
        print("用户信息: {}".format(rs.group()))
    else:
        print("用户信息不完整!")
