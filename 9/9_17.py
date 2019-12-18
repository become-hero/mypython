import json
with open("./user_info.json","r")as f:
    user_info_dict=json.load(f)
    print(user_info_dict)
