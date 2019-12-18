import json
user_info_dict={"name":"zhangsan",
                "age":20,
                "language":["python","java"],
                "study":{"AI":"python","bigdata":"hadoop"},
                "if_vip":True,
                "gender":None}
json_str=json.dumps(user_info_dict)
print(json_str)
