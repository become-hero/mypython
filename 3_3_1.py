user_info_dict={"name":"tom","age":"20","gender":"male","program":"python"}
#program=user_info_dict["tel"]
#print("tel:{}".format(tel))
tel=user_info_dict.get("tel","10086")
print("tel:{}".format(tel))
