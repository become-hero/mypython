student_id_set={"1111","2222","3333","4444"} 
student_id_set.add("5555")
print(student_id_set)

student_id_set.update(["6666","7777","6666"])
print("update 列表",student_id_set)

student_id_set.update(("8888","9999"))
print("update 元组",student_id_set)

student_id_set_new={"010","011"}
student_id_set.update(student_id_set_new)
print("update 合并集合",student_id_set)

student_id_set.update(["012","013"],["013","014","015"])
print("update 合并序列",student_id_set)

student_id_set.update("0123456789")
print("update 字符串",student_id_set)
