def x_y_compute(x,y,func):
    print("x={}".format(x))
    print("y={}".format(y))
    result=func(x,y)
    print("result={}".format(result))
x_y_compute(3,5,lambda x,y:x+y)
x_y_compute(3,5,lambda x,y:x*y)
