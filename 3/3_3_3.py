user_info_dict={"name":"tom","age":"20","gender":"male","program":"python"}
'''user_info_dict["tel"]="13300000000"
print(user_info_dict)
tel=user_info_dict.get("tel","10086")
print("tel:{}".format(tel))
#add dict
user_info_dict["tel"]="11111111"
#查询健的值
tel=user_info_dict.get("tel","10086")
print("old tel:{}".format(tel))
user_info_dict["tel"]="22222222"
tel=user_info_dict.get("tel","10086")
print("new tel:{}".format(tel))
print("before: ",user_info_dict)
del user_info_dict["tel"]
print(" after: ",user_info_dict)
for key in user_info_dict.keys():
    print("{}:{}".format(key,user_info_dict[key]))
for value in user_info_dict.values():
    print(value)
for item in user_info_dict.items():
    print("--------------")
    print("item类型: ",type(item))
    print("item:",item)
    print(item[0])
    print(item[1])
    '''
for key,value in user_info_dict.items():
    print("{}:{}".format(key,value))
