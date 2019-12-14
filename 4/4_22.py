#!/usr/bin/python3
import sys
def time_counter(func):
    def counter(*args):
        print("------start--------")
        #start_time=time.time()
        #print("start_time:",start_time)
        func(*args)
        print("-----end----")
        #end_time=time.time()
        #print("end_time:",end_time)
        #print("run_times:",end_time-start_time)
        return
    return counter
@time_counter
def  sum(x,y):
    #time.sleep(2)
    print("{}+{}={}".format(x,y,x+y))
    return
@time_counter
def multiplied(x,y,z):
    print("{}*{}*{}={}".format(x,y,z,x*y*z))
    return
sum(10,20)
multiplied(4,5,6)
