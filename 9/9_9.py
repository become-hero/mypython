with open("stu.txt","r",encoding="utf-8")as f:
    lines=f.readlines()
    print(lines)
    for i in range(0,len(lines)):
        print("line={}  {}".format(i,lines[i]),end="")
