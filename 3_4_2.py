student_id_set={"1111","2222","3333","4444"}
student_id="2222"
if student_id in student_id_set:
    print("{}学号存在！".format(student_id))

student_id="8888"
if student_id not in student_id_set:
    print("{}学号不存在!".format(student_id))
