def counter_func(base=0,step=1):
    return base+step
c1=counter_func()
print("------------------{}".format(c1))
c2=counter_func(c1)
print("------------------{}".format(c2))
c3=counter_func(c2)
print("------------------{}".format(c3))
