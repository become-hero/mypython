def yiliao(basic,**kvargs):
    health=kvargs.get("health")
    pension=kvargs.get("pension")
    cost=basic*health+basic*pension
    return cost

def tax(balance):
    if balance <=5000:
        ret=0
    elif balance>5000 and balance<=10000:
        ret=balance*0.05
    elif balance>10000:
        ret=balance*0.1
    else:
        ret=balance*0.2
    return ret

def pay(basic):
    cost_dict={"health":0.02,"pension":0.08}
    cost=yiliao(basic,**cost_dict)
    balance=basic-cost
    tax_fee=tax(balance)
    pay_fee=basic-cost-tax_fee
    print("基本工资：{}社保交费：{}个人所的税：{}实际发工资：{}".format(basic,cost,tax_fee,pay_fee))
    return
pay(8000)
