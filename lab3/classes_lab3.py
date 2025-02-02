import math
import random
def filt(num):
    if num < 2:
        return False
    for i in range(2, int(pow(num, 0.5))+1):
        if num % i == 0:
            return False
    return True

arr = [random.randint(1,10) for i in range(10)]
print(arr)
nums = list(filter(lambda x: filt(x), arr))
print(nums)