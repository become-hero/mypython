print("准备打开一个文件")
try:
    open("test.txt")
    print("打开文件成功!")
except FileNotFoundError as err:
    print("发现异常，文件不存在!")
print("程序即将结束.")
