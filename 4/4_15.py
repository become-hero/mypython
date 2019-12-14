def sum(x,y):
    return x+y

def sum_closure(x):
    def sum_inner(y):
        return x+y
    return sum_inner

rs1=sum(10,1)
print("rs1={}".format(rs1))
print("rs1 type: {}".format(type(rs1)))
print("-------------------------------------")
rs_func=sum_closure(10)
print("rs_func={}".format(rs_func))
print("rs_func type={}".format(type(rs_func)))
print("-------------------------------------")
rs2=rs_func(1)
print("rs2={}".format(rs2))
print("rs2 type is{}".format(type(rs2)))
