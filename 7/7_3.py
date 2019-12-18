try:
    print(num)
    open("test.txt")
except (NameError,FileNotFoundError) as err:
    print("发现了异常!",err)
print("----END----")
