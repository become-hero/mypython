'''
    info_lists=[["tom",20,180.5,80,True],["jam",18,175,70,True],["mark",25,185,90,False]]
print(info_lists[0])

print("所有同学名字：")
print(info_lists[0][0])
print(info_lists[1][0])
print(info_lists[2][0])
new_info=["kilo",25,190,85,False]
info_lists.append(new_info)
print(info_lists)
new_info=["kk",25,190,85,False]
info_lists.insert(1,new_info)
print(info_lists)

new_info_lists=[["wawa",25,190,85,False],["niuniu",23,170,70,False]]
info_lists.extend(new_info_lists)
print(info_lists)
'''
name_list1=["11","22","33"]
name_list2=["44","55"]
name_list3=name_list1+name_list2
print("name_list1",name_list1)
print("name_list2",name_list2)
print("name_list3",name_list3)
