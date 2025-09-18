#Jc 2nd I want to test the import time stuff

import time
import datetime as dt

current_time = time.time()
readable_time = time.ctime(current_time)



print(f"{current_time}")
print(readable_time)
#Time.time

now = dt.datetime.now()
hour = now.strftime("%H")
print(hour)
print(f"My hour varible is a string: {isinstance(hour,str)}" )