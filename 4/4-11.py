basic_value=1000
def sum(x):
    global basic_value
    basic_value=1500
    rs=basic_value+x
    print("{}+{}={}".format(basic_value,x,rs))
    return
def product(x):
    rs=basic_value*x
    print("{}*{}={}".format(basic_value,x,rs))
    return

print("basic_value: ",basic_value)
sum(20)
print("basic_value: ",basic_value)
product(20)
