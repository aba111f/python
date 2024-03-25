import datetime
import math

x = datetime.datetime.now()
y = datetime.datetime(2014, 2, 20, 10, 42, 59)


print((x - y).total_seconds()) 
print(abs((x).second - y.second))