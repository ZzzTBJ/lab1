#5.12
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
x = thisset.pop()
print(x)

print(thisset)