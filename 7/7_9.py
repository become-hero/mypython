def div(a,b):
    if b==0:
        raise ZeroDivisionError("除数不能为0")
    else:
        return a/b
div(2,0)
