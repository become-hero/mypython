'''num_list=[10,20,30,40]
any_num_sum=(*num_list)
print("----------")
'''
fee_dict={"tax":500,"social":1500}
pay(8000,**fee_dict)
print("vargs->value: ",kvargs)
print("vargs->type : ",type(kvargs))
print("实发工资：{}".format(pay))
