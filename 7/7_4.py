try:
    open("test.txt")
    print(num)
except NameError as err:
    print("发现了异常：",err)
except Exception as err_all:
    print("发现了全部异常",err_all)
