from math import *
#1
deg = int(input("Input degree: "))
print("Output radian:",radians(deg))
#2
h = int(input("Height: "))
b1 = int(input("Base, first value: "))
b2 = int(input("Base, second value: "))
S = ((b1+b2)/2)*h
print("Expected Output:", S)
#3
n = int(input("Input number of sides: "))
l = int(input("Length of a side: "))
ap = l/(2*(tan(pi/n)))
p = l*n
s1 = (ap*p)/2
print("The area of the polygon is:", round(s1))
#4
l1 = int(input("Length: "))
h1 = int(input("Height: "))
s2 = l1*h1
print("Expected Output:", s2)
