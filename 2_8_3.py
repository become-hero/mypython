#!/usr/bin/python3
fee=input("请叫费用50元：")
fee_int=int(fee)
if fee_int==50:
    print("成功！！")
    gender=input("girl or boy: {g|b}")
    if gender=="b":
        print("boy line,Pls wait.")
    elif gender=="g":
        print("girl line,Pls wait")
else:
    print("sorry,can not undersdent!")
