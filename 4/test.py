def num_sum(*args):
    print("value-> ",args)
    print("type->  ",type(args))
    rs=0
    if len(args)>0:
        for arg in args:
            rs+=arg
    print("total: {}".format(rs))
    return
num_sum(20,30,40)
num_list=[2,3,4,5,6]
num_sum(*num_list)
