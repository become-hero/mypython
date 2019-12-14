stuscore={}
def if_admin(admin):
    def check(func):
        def inner(t_name,s_name,score):
            print("正在进行权限检查......")
            if t_name != admin:
                raise Exception("权限不够！禁止操作")
            func(t_name,s_name,score)
            print("操作成功")
        return inner
    return check
#add
@if_admin("admin")
def add_stu_score(t_name,s_name,score):
    stuscore[s_name]=score

#
@if_admin("admin")
def update_stu_score(t_name,s_name,score):
    stuscore[s_name]=score

add_stu_score("admin","tom",100)
print(stuscore)
add_stu_score("admin","tom",99)
print(stuscore)
add_stu_score("derek","david",40)
print(stuscore)
