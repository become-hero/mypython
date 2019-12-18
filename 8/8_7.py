import time
for t in range(3,-1,-1):
    print("start: ",t)
    if t!=0:
        time.sleep(1)
    else:
        print("Go!")
