def any_num_sum(*args):
    print("args->value: ",args)
    print(" args->type: ",type(args))
    rs=0
    if len(args)>0:
        for arg in args:
            rs+=arg
    print("total: {}".format(rs))
    return
any_num_sum(20,30)
any_num_sum(20,30,40,50)
any_num_sum(20,30,40,50,60,70)

num_list=[10,20,30,40]
any_num_sum(*num_list)
