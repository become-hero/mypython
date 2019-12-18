#line="hello world hello python"
'''
print(line.find("world"))
print(line.find("hello"))
print(line.find("hello",6))
print(line.find("zhangsan"))
print(line.count("hello"))
new_line=line.replace("hello","hi")
print("    line:",line)
print("new_line:",new_line)
new_line2=line.replace("hello","hi",1)
print("    line:",line)
print("new_line2:",new_line2)
split_list=line.split(" ")
print("line:",line)
print("split:",split_list)

split_list2=line.split(" ",1)
print("line:",line)
print("split2:",split_list2)
print(line.startswith("hello"))
print(line.endswith("python"))
content=input("pls input yes|no: ")
print("message: ",content)
if content.lower()=="yes":
    print("welcome using.")
else:
    print("exit.")
print("+".join(["xiaoming",str(20),"beijing"]))
'''
print("   sss   ".strip())
#
print("\tsss\t".strip())
#
print("\nsss\n".strip())
#
print(",,,sss,,,".strip(","))
