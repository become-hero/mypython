def pay(basic,**kvargs):
    print("vargs->value: ",kvargs)
    print("vargs->type : ",type(kvargs))
    tax=kvargs.get("tax")
    social=kvargs.get("social")
    pay=basic-tax-social
    print("实发工资：{}".format(pay))
pay(8000,tax=500,social=1500)
fee_dict={"tax":500,"social":1500}
pay{8000,**fee_dict}
