#1
num = int(input("Square up to: "))
def Square(n):
    for i in range(n+1):
        yield i*i
a = Square(num)
for i in a:
    print(i)
#2
num1 = int(input("Even numbers: "))
def Even(n):
    for i in range(n+1):
        if (i%2 == 0):
            yield i
a1 = Even(num1)
for j in a1:
    print(j, end=', ')
#3
print(" ")
num2 = int(input("Divisible: "))
def Divisible(n):
    for i in range(n+1):
        if(i%3 == 0) and (i%4 == 0):
            yield i
a2 = Divisible(num2)
for i in a2:
    print(i)
#4
def squares(a,b):
    for i in range(a,b+1):
        yield i*i
for i in squares(int(input("A: ")), int(input("B: "))):
    print(i)
#5
def Numbers(n):
    for i in range(n, -1, -1):
        yield i
for i in Numbers(int(input("Decrease from: "))):
    print(i)
        