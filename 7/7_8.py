def func1():
    print("----test1-1----")
    print(num)
    print("----test1-2----")
def func2():
    try:
        print("----test2-1----")
        func1()
        print("----test2-2----")
    except Exception as err:
        print("发现了异常",err)
        print("----test2-3----")
func2()
