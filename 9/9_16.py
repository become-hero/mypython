import json
user_info_dict={"name":"zhangsan",
    "age":20,
    "language":["python","java"],
    "study":{"AI":"python","bigdata":"hadoop"},
    "if_vip":True,
    "gender":None}
with open("./user_info.json","w")as f:
    json.dump(user_info_dict,f)
