def counter_closure(base=0):
    cnt_base=[base]
    def counter(step=1):
        cnt_base[0]+=step
        return cnt_base[0]
    return counter
temp=counter_closure()
print("total: {}".format(temp()))
print("total: {}".format(temp()))
print("total: {}".format(temp()))
print("type is {}".format(type(temp())))
