import json
json_str=(
            "name":"zhangsan", 
            "age":20, 
            "language":["python", "java"], 
            "study":{
                    "AI":"python", 
                    "bigdata":"hadoop"
                    }, 
            #"if_vip":true, 
            #"gender":null
            )
python_dict=json.loads(json_str)
print("转换之后的类型{}".format(type(python_dict)))
print(python_dict)
