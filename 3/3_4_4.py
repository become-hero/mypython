student_id_set={"1111","2222","3333","4444"} 
'''
student_id_set.remove("1111")
print("remove()执行后",student_id_set)
student_id_set.remove("1111")
student_id_set.discard("1111")
print("doing after:",student_id_set)
student_id_set.discard("1111")
print("again      :",student_id_set)'''
item=student_id_set.pop()
print("pop() later:",student_id_set)
print("delate     :",item)
