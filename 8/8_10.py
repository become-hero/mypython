import datetime
import time
start_time=datetime.datetime.now()
print("start---------",start_time)
time.sleep(2)
end_time=datetime.datetime.now()
print("end------------",end_time)
print("时间差：{}".format(end_time.second-start_time.second))
