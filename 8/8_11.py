import time
import datetime

#format_time=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#print("diy: {}".format(format_time))
ts=time.time()
print(datetime.datetime.fromtimestamp(ts))
print(datetime.datetime.fromtimestamp(ts).strftime("%Y/%M/%d %H:%M:%S"))
