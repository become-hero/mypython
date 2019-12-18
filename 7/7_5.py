try:
    f=open("test.txt")
    print("打印文件")
#except FileNotFoundError as err:
#    print("发现了异常",err)
finally:
    print("关闭连接")
