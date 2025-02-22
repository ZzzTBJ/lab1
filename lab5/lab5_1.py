import re
#1
txt = input("Your 1 string: ")
x = re.search("a[b]*", txt)
if x:
    print("Yes, found match")
else:
    print("There is no match")
#2
txt1 = input("Your 2 string: ")
x1 = re.search("a[b]{2,3}", txt1)
if x1:
    print("Yes, found match")
else:
    print("There is no match")
#3
txt2 = input("Your 3 string: ")
x2 = re.search("[a-z]+_[a-z]", txt2)
if x2:
    print("Yes, found match")
else:
    print("There is no match")
#4
txt3 = input("Your 4 string: ")
x3 = re.search("[A-Z]{1}[a-z]", txt3)
if x3:
    print("Yes, found match")
else:
    print("There is no match")
#5
txt4 = input("Your 5 string: ")
x4 = re.search("a.*b$", txt4)
if x4:
    print("Yes, found match")
else:
    print("There is no match")
#6
txt5 = "Hello, Zukhra."
x5 = re.search("[ ,.]", txt5)
if x5:
    print("Yes, found match", re.sub(r'[ ,.]', ":", txt5))
else:
    print("There is no match")
#7
txt6 = "snake_case_example"
x6 = re.search("_(.)", txt6)
print("Camel string: ", re.sub(r'_(.)', x6.group(1).upper(), txt6))
#8
txt7 = input("String 8: ")
x7 = re.split(r'[A-Z]', txt7)
print(x7)
#9
txt8 = input("String 9: ")
x8 = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt8)
print(x8)
#10
txt10 = "camelCaseExample"
x10 = re.sub("([a-z])([A-Z])", r'\1_\2',txt10)
print(x10.lower())