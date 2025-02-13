#1
from datetime import *
print(datetime.now().day - 5)
#2
print("Yesterday: ", (datetime.today() - timedelta(days=1)).strftime('%a'))
print("Today: ", (datetime.today()).strftime('%a'))
print("Tomorrow: ", (datetime.today() + timedelta(days=1)).strftime('%a'))
#3
print(datetime.now().strftime("%x %X"))
#4
x1 = datetime.now()
x2 = datetime(2025, 1, 1)
d = x1-x2
print(d.total_seconds())