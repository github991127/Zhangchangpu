'''
import calendar

cal = calendar.month(2021, 3)
print("以下输出2021年3月份的日历:")
print(cal)


import time

ticks = time.time()
print("当前时间戳为:", ticks)
localtime = time.localtime()
print ("本地时间为 :", localtime)
localtime = time.asctime( time.localtime() )
print ("本地时间为 :", localtime)
localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print ("本地时间为 :", localtime)



import math
import cmath#复数

print(math.e)
print(cmath.sqrt(math.e))
'''
