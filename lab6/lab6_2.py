import math
import time
def mult(l):
    return math.prod(l)
def summ(s):
    sum1 = 0
    sum2 = 0
    for i in s:
        if i.isupper():
            sum1 = sum1 + 1
        if i.islower():
            sum2 = sum2 + 1
    return {"uppercase":sum1, "lowercase": sum2}
def pal(s):
    return s == s[::-1]
def sq(num, t):
    time.sleep(t/1000)
    return math.sqrt(num)
def tup(l):
    return all(l)
print("Multiplication:", mult([1,2,3]))
print(summ("HelloWorld"))
print("Palindrome: ", pal("madam"), pal("loh"))
print("Sqrt of 16 after 4 milliseconds:", sq(16, 4))
print("Tuple: ", tup((False, True, True)))
print("Tuple: ", tup((True, True, True)))