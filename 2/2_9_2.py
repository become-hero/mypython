i = 1
n = 4
while i <= n:
    print(" "*(n-i),end="")
    j = 1
    while j <= 2*i-1:
        print("*",end="")
        j += 1
    print("")
    i += 1
