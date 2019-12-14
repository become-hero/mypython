def pay(basic,**kvargs):
    print("vaule-> ",kvargs)
    print("type->  ",type(kvargs))
    tax=kvargs.get("tax")
    social=kvargs.get("social")
    pay=basic-tax-social
    print("all money:{}".format(pay))
    return
my_dict={"tax":500,"social":1500}
pay(8000,**my_dict)
