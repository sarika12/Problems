import time
import datetime

date=datetime.datetime.today()
print(date)
current_time=time.time()
print(current_time)

current_time1=time.ctime()
print(current_time1)

formate_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

print(formate_time)