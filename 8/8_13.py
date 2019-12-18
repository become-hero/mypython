import time
import datetime
today=datetime.datetime.today()
print("今天的日期：{}".format(today.strftime("%Y-%m-%d")))
days=datetime.timedelta(days=1)
yesterday=today-days
print("昨天的日期：{}".format(yesterday.strftime("%Y-%m-%d")))
